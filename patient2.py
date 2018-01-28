# from bigchaindb_driver import BigchainDB
# from bigchaindb_driver.crypto import generate_keypair
from twilio.rest import Client
class patient2:

    def __init__(self, patientFirstName, patientLastName, diagnosis, diagnosisDate, conditionStart):
        self.name = patientFirstName + patientLastName
        self.blockchain = []
        self.currentNode = 0
        self.createBlock(diagnosis, diagnosisDate, conditionStart)
        #print "nacho"


    def createBlock(self, diagnosis, diagnosisDate, conditionStart):
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

        self.blockchain.append(block_asset)
        self.sendInfo(self.blockchain[self.currentNode])
        self.currentNode = self.currentNode + 1

    def getName(self):
        return(self.name)

    def sendInfo(self, stuff):
        print (stuff)
        self.sendMessage("7853200582", "7165314545", stuff)


    def sendMessage(self,toNumber, fromNumber, message):
        account_sid = "AC9b64644cb7c33ef1467ab5fba7aa385f"

        auth_token  = "b88f5ffb3a8fe815538506ebed83b3d6"

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            to = toNumber,
            from_ = fromNumber,
            body = message)
