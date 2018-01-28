from bigchaindb_driver import BigchainDB from bigchaindb_driver.crypto import generate_keypair
from twilio.rest import Client
class patient2:

    def __init__(self, patientFirstName, patientLastName, diagnosis, diagnosisDate, conditionStart):
        self.name = patientFirstName + patientLastName
        self.blockchain = []
        self.currentNode = 0
        self.createBlock(diagnosis, diagnosisDate, conditionStart)
        ##print "nacho"


    def createBlock(self, diagnosis, diagnosisDate, conditionStart):
        parent = generate_keypair()

        tokens = {}
        tokens['app_id'] = 'c3080fbc'
        tokens['app_key'] = 'cdf98e4878062f34c2da1b94fab0b009'
        bdb = BigchainDB('http://35.196.237.62:9984/', headers=tokens)#localhost:9984
        #number = key

        block_asset = {
        'data': {
        'diagnosis': diagnosis,
        'diagnosisDate': diagnosisDate,
        'conditionStart': conditionStart,
                },
        'link': {
        'Current': self.currentNode,
        'Next': self.currentNode + 1
                }

        }

        #print(bdb.assets.get(search=str(currentNode)))

        prepared_creation_tx = bdb.transactions.prepare(
            operation='CREATE',
            signers=parent.public_key,
            asset=block_asset,
        )

        fulfilled_creation_tx = bdb.transactions.fulfill(
            prepared_creation_tx,
            private_keys=parent.private_key
        )

        sent_creation_tx = bdb.transactions.send(fulfilled_creation_tx)


        self.blockchain.append(fulfilled_creation_tx)
        self.sendInfo(self.blockchain[self.currentNode])
        self.currentNode = self.currentNode + 1

    def getName(self):
        return(self.name)

    def sendInfo(self, stuff):
        #print (stuff)
        self.sendMessage("7853200582", "7165314545", stuff)


    def sendMessage(self,toNumber, fromNumber, message):
        account_sid = "AC9b64644cb7c33ef1467ab5fba7aa385f"

        auth_token  = "b88f5ffb3a8fe815538506ebed83b3d6"

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            to = toNumber,
            from_ = fromNumber,
            body = message)
