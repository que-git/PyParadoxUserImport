
class Employee:
    id = 0
    first_name = ""
    surname = ""
    card = ""
    evidence = ""

    def __init__(self,UID, FN, SN, Card, Evidence):
        self.id = UID
        self.first_name = FN
        self.surname = SN
        self.card = Card
        self.evidence = Evidence

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return self.first_name.ljust(20,' ')+self.surname.ljust(20,' ')+str(self.id).ljust(10,' ')+str(self.card).ljust(20,' ')+str(self.evidence).ljust(10,' ')
