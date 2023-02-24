class Subject:
    def __init__ (self, subName, subCode, credHr):
        self.subName = subName
        self.subCode = subCode
        self.credHr = credHr

    def getSubject(self):
        print ("Subject Name: " + self.subName + "\nSubject Code: " + self.subCode + "\nCredit Hour: " + self.credHr)