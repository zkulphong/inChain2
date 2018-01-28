from run import run

asdf = run({"doctorfirstname": "0", "doctorlastname": "0", "patientfirstname": "0", "patientlastname": "0", "diagnosis": "0", "diagnosisdate": "0", "conditionstart": "0"})

def addBlock(data):
    asdf.parse(data)
