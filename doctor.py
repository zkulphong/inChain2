from patient2 import patient2

class doctor:
    def __init__(self, doctorFirstName, doctorLastName, patientFirstName, patientLastName, diagnosis, diagnosisDate, conditionStart):
        self.name = doctorFirstName + doctorLastName
        self.patients= []
        self.addPatient(patientFirstName, patientLastName, diagnosis, diagnosisDate, conditionStart)
        ##print "taco"

    def addPatient(self, patfirstname, patlastname, diagnosis, diagnosisDate, conditionStart):
        #print "lol"
        check_pat = True
        count = 0
        index = 0
        while index < len(self.patients):
            if (patfirstname + patlastname in self.patients[index].getName()):
                #print "dorito"
                check_pat = False
                count = index
            index = index + 1
        if check_pat == True:
            new_patient = patient2(patfirstname, patlastname, diagnosis, diagnosisDate, conditionStart)
            self.patients.append(new_patient)

        else:
            self.patients[count].createBlock(diagnosis, diagnosisDate, conditionStart)

    def getName(self):
        return(self.name)
