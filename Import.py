from Employee import Employee
import DB
import pypxlib



print('Looking for Paradox files at "src/paradox"...')
try:
    paradox_users = pypxlib.Table('paradox/Users.DB')
    paradox_evidence = pypxlib.Table('paradox/Transponder Codes.DB')
except pypxlib.PXError as err:
    print('Error opening paradox files. ',err)
    exit(-2)

cards = {}

employees_new = []
employees_exist = []
employees_import = []

# print(paradox_evidence.fields)
#print(paradox_users.fields)
for row in paradox_evidence:
    cards[row['UserID']] = str(int('0x'+row['Code'],0)).rjust(13,"0")
    # print(paradox_users.fields)

no_card = 0
for row in paradox_users:
    try:
        if row['Active']:
            person = Employee(row['UserID'], row['FirstName'], row['LastName'], cards[row['UserID']], str(row['Evidence']))
            employees_new.append(person)
            #print(row['UserID'], row['FirstName'], row['LastName'], cards[row['UserID']], row['Active'], row['Status'])
    except KeyError:
        no_card += 1
print('Paradox contains', str(len(employees_new)) ,'users.')

if no_card > 0:
    print(no_card, "users dont have assigned cards.")

employees_exist = DB.getUsers()
for new in employees_new:
    if not employees_exist.__contains__(new):
        employees_import.append(new)

command = ''
while command != 'q' or command != 'i':
    command = input("Press 'q' to quit, 's' to show new users, 'i' to import "+str(len(employees_import))+" new users\n>")
    if command == 'q':
        print('Bye!')
        exit(0)
    if command == 's':
        print("Name".ljust(20)+"\tSurname".ljust(30)+"\tID".ljust(20)+"\tCard".ljust(30)+"\tEvidence".ljust(30))
        for user in employees_import:
            print(user)
    if command == 'i':
        for user in employees_import:
            print("Importing: "+str(user))
            DB.addUser(user)
        exit(0)
