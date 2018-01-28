from doctor import doctor
from patient2 import patient2

class run:

    def __init__(self, data):
        self.doctors = []
        self.parse(data)
        print self.doctors[0].getName()
        #print "test"

    def parse(self, data):
        doctorFirstName = data['doctorfirstname']
        doctorLastName = data['doctorlastname']
        patientFirstName = data['patientfirstname']
        patientLastName = data['patientlastname']
        diagnosis = data['diagnosis']
        diagnosisDate = data['diagnosisdate']
        conditionStart = data['conditionstart']

        check_doc = True
        count = 0
        index = 0
        print index
        while index < len(self.doctors):
            print index
            if (doctorFirstName + doctorLastName in self.doctors[index].getName()):
                print "horse"
                check_doc = False
                count = index
            index = index + 1

        if check_doc == True:
            new_doctor = doctor(doctorFirstName, doctorLastName, patientFirstName, patientLastName, diagnosis, diagnosisDate, conditionStart)
            self.doctors.append(new_doctor)

        else:
            print "tostito"
            self.doctors[count].addPatient(patientFirstName, patientLastName, diagnosis, diagnosisDate, conditionStart)
