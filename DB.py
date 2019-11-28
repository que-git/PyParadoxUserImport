import pyodbc
import Employee

def getUsers():
    employees_db = []

    askDate = query("SELECT GETDATE()")
    for row in askDate:
        print("Server time", row[0])


    askESD = query(" SELECT PU.[FName], PU.[SName], PU.[UID], PT.[Code], PU.[Evidence] "
                   " FROM [TechniESD].[dbo].[Paradox_Users] PU "
                   " LEFT JOIN [TechniESD].[dbo].[Paradox_transponder] PT ON PT.UID = PU.UID ")
    for row in askESD:
        person = Employee.Employee(row[2], row[0], row[1], row[3], row[4])
        employees_db.append(person)

    return employees_db


def addUser(employ):
    query_str = "exec [TechniESD].[dbo].[AddUser] "+str(employ.id)+", '"+employ.first_name+"', '"+employ.surname+"', '"+employ.card+"', '"+employ.evidence+"'"
    #print(query_str)
    query(query_str).commit()

def query(queryString):
    db_host = ""
    ESDdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + db_host + ';UID=;PWD=')
    askDate = ESDdb.cursor()
    askDate.execute(queryString)
    return askDate
