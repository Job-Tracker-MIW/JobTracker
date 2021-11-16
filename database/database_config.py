import mysql.connector
import os
from dotenv import load_dotenv
import datetime
from dateutil import parser

load_dotenv()

# Get the environment variables where sensitive logon information securely stored
config = {
    'user': os.environ.get('DB_USER'),
    'password': os.environ.get('DB_PASSWORD'),
    'host': os.environ.get('DB_HOST'),
    'database': os.environ.get('DB_DATABASE')
    }

def createAndSeedTables():
    mydb = mysql.connector.connect(**config)
    mycursor = mydb.cursor()

    # drop tables

    mycursor.execute("DROP TABLE IF EXISTS JobsSkills")
    mycursor.execute("DROP TABLE IF EXISTS Applications")
    mycursor.execute("DROP TABLE IF EXISTS Skills")
    mycursor.execute("DROP TABLE IF EXISTS Jobs")
    mycursor.execute("DROP TABLE IF EXISTS Contacts")
    mycursor.execute("DROP TABLE IF EXISTS Users")
    mycursor.execute("DROP TABLE IF EXISTS Companies")

    # create tables
    sql = "CREATE TABLE Users (userid INT AUTO_INCREMENT PRIMARY KEY,\
    username VARCHAR(50) NOT NULL, password VARCHAR(25) NOT NULL, email VARCHAR(50) NOT NULL)"
    mycursor.execute(sql)

    sql = "CREATE TABLE Companies (companyid INT AUTO_INCREMENT PRIMARY KEY, company VARCHAR(50) NOT NULL) ENGINE=InnoDB AUTO_INCREMENT=1000;"
    mycursor.execute(sql)

    sql = "CREATE TABLE Jobs (jobid INT AUTO_INCREMENT PRIMARY KEY,\
    userid INT NOT NULL, name VARCHAR(50) NOT NULL, title VARCHAR(50) NOT NULL, companyid INT NOT NULL,  CONSTRAINT job_name UNIQUE (companyid, title, name),\
    FOREIGN KEY(userid) REFERENCES Users(userid) ON DELETE CASCADE, FOREIGN KEY(companyid) REFERENCES Companies(companyid) ON DELETE CASCADE)"
    mycursor.execute(sql)

    sql = "CREATE TABLE Applications (appid INT AUTO_INCREMENT PRIMARY KEY,\
    jobid INT NOT NULL, userid INT NOT NULL, name VARCHAR(50) NOT NULL, status VARCHAR(50) NOT NULL, application_date DATE NOT NULL,\
    FOREIGN KEY(jobid) REFERENCES Jobs(jobid) ON DELETE CASCADE, FOREIGN KEY(userid) REFERENCES Users(userid) ON DELETE CASCADE)"
    mycursor.execute(sql)

    sql = "CREATE TABLE Skills (skillid INT AUTO_INCREMENT PRIMARY KEY,\
    userid INT NOT NULL, name VARCHAR(50) NOT NULL, proficiency VARCHAR(25) NOT NULL,\
    FOREIGN KEY(userid) REFERENCES Users(userid) ON DELETE CASCADE)"
    mycursor.execute(sql)

    sql = "CREATE TABLE JobsSkills (id INT AUTO_INCREMENT PRIMARY KEY,\
    skillid INT NOT NULL, jobid INT NOT NULL, FOREIGN KEY(skillid) REFERENCES Skills(skillid) ON DELETE CASCADE,\
    FOREIGN KEY(jobid) REFERENCES Jobs(jobid) ON DELETE CASCADE)"
    mycursor.execute(sql)

    sql = "CREATE TABLE Contacts (contactid INT AUTO_INCREMENT PRIMARY KEY,\
    userid INT NOT NULL, name VARCHAR(50), companyid INT, email VARCHAR(50), phone VARCHAR(15),\
    FOREIGN KEY(userid) REFERENCES Users(userid) ON DELETE CASCADE, FOREIGN KEY(companyid) REFERENCES Companies(companyid) ON DELETE CASCADE)"
    mycursor.execute(sql)



    mydb.commit()
    mycursor.close()

    mycursor = mydb.cursor(buffered=True)

    # seed tables with dummy data
    sql = "INSERT INTO Users (username, password, email) VALUES (%s, %s, %s)"
    val = ("someuser", 12345, "someuser@test.com")
    mycursor.execute(sql, val)

    sql = "insert into Companies (company) values (%s)"
    val = ("faangermmaigawd",)
    mycursor.execute(sql, val)

    sql = "insert into Companies (company) values (%s)"
    val = ("Oregon State University",)
    mycursor.execute(sql, val)

    sql = "insert into Companies (company) values (%s)"
    val = ("Microsoft",)
    mycursor.execute(sql, val)



    sql = "select companyid from Companies"
    mycursor.execute(sql)
    val = mycursor.fetchone()
    val2 = mycursor.fetchone()
    companyid = val[0]
    companyid2 = val2[0]

    sql = "select userid from Users"
    mycursor.execute(sql)
    val = mycursor.fetchone()
    userid = val[0]

    sql = "INSERT INTO Skills (userid, name, proficiency) VALUES (%s, %s, %s)"
    val = (int(userid), "Javascript", "2")
    mycursor.execute(sql, val)

    sql = "INSERT INTO Skills (userid, name, proficiency) VALUES (%s, %s, %s)"
    val = (int(userid), "Python", "8")
    mycursor.execute(sql, val)

    sql = "INSERT INTO Skills (userid, name, proficiency) VALUES (%s, %s, %s)"
    val = (int(userid), "C++", "6")
    mycursor.execute(sql, val)



    sql = "INSERT INTO Jobs (userid, name, title, companyid) VALUES (%s, %s, %s, %s)"
    val = (int(userid), "Hope I get it", "Software Engineer I", int(companyid))
    mycursor.execute(sql, val)

    sql = "INSERT INTO Jobs (userid, name, title, companyid) VALUES (%s, %s, %s, %s)"
    val = (int(userid), "looks good!", "Software Engineer II", int(companyid2))
    mycursor.execute(sql, val)

    # sql = "INSERT INTO Jobs (userid, name, title, companyid) VALUES (%s, %s, %s, %s)"
    # val = (int(userid), "A start", "Jr. Software Engineer", int(companyid2))
    # mycursor.execute(sql, val)



    sql = "select jobid from Jobs"
    mycursor.execute(sql)
    val = mycursor.fetchone()
    val2 = mycursor.fetchone()
    jobid = val[0]
    jobid2 = val2[0]

    sql = "INSERT INTO Applications (jobid, userid, name, status, application_date) VALUES (%s, %s, %s, %s, %s)"
    val = (int(jobid), int(userid), "First Application", "Applied", datetime.date(2021,10,1))
    mycursor.execute(sql, val)

    sql = "INSERT INTO Applications (jobid, userid, name, status, application_date) VALUES (%s, %s, %s, %s, %s)"
    val = (int(jobid2), int(userid), "Second Application", "Applied", datetime.date(2021,10,10))
    mycursor.execute(sql, val)


    sql = "select skillid from Skills"
    mycursor.execute(sql)
    val = mycursor.fetchone()
    skillid = val[0]

    sql = "INSERT INTO JobsSkills (skillid, jobid) VALUES (%s, %s)"
    val = (int(skillid), int(jobid))
    mycursor.execute(sql, val)

    sql = "INSERT INTO Contacts (userid, name, companyid, email, phone) VALUES (%s, %s, %s, %s, %s)"
    val = (int(userid), 'John Doe', int(companyid), 'jdoe@gfaangermaigawd.com', '555-555-5555')
    mycursor.execute(sql, val)

    sql = "INSERT INTO Contacts (userid, name, companyid, email, phone) VALUES (%s, %s, %s, %s, %s)"
    val = (int(userid), 'Jane Smith', int(companyid2), 'jdoe@osu.edu.com', '555-555-5555')
    mycursor.execute(sql, val)

    sql = "select contactid from Contacts"
    mycursor.execute(sql)
    val = mycursor.fetchone()
    contactid = val[0]



    mydb.commit()
    mycursor.close()
    mydb.close()


def getTableApplications(userid):
    mydb = mysql.connector.connect(**config)
    cur = mydb.cursor(dictionary=True)

    sql = "SELECT a.appid, b.title AS title, c.company AS company, a.status AS status, a.application_date AS appdt FROM Applications a LEFT JOIN Jobs b ON " + \
          " a.jobid = b.jobid LEFT JOIN Companies c on b.companyid = c.companyid WHERE a.userid = %s"
    
    cur.execute(sql, (userid,))

    vals = cur.fetchall()

    mydb.close()
    return(vals)

# I just stubbed this for testing the Companies Applied page. we can delete later
# and use Mat's implementation.
def addToApplied(userid, application, curr_datetime):
    #mydb = mysql.connector.connect(**config)
    #cur = mydb.cursor(dictionary=True)
    #jobid = applied_attributes["jobid"]
    #application_date = curr_datetime
    #name = "Another Application 1"
    #status = "Applied"
#
#    sql = """INSERT INTO Applications (userid, jobid, name, status, application_date) 
#                VALUES (%s, %s, %s, %s, %s)"""
#
#    val = (int(userid), int(jobid), name, status, application_date)
#    cur.execute(sql, val)
#
#    mydb.commit()
#    cur.close()
#    mydb.close()

    mydb = mysql.connector.connect(**config)
    cur = mydb.cursor(dictionary=True)

    title = application["title"]
    company = application["company"]
    name = application["name"]
    
    if 'status' in application.keys():
        status = application["status"]
    else: status = 'Applied'
    #appdt = curr_datetime #parser.parse(application["appdt"])
    appdt = parser.parse(curr_datetime)

    # need to make sure company exists otherwise should add company
    sql = "select companyid from Companies where company = %s"
    cur.execute(sql, (company,))
    companyid = cur.fetchall()
    if len(companyid) > 0:
        companyid = companyid[0]['companyid']


        # if job doesn't exist need to add
        sql = "select jobid from Jobs where title = %s and companyid = %s and name = %s"
        cur.execute(sql, (title, companyid, name))
        jobid = cur.fetchall()
        if len(jobid) > 0:
            jobid = jobid[0]['jobid']
        else:
            sql = "INSERT INTO Jobs (userid, name, title, companyid) VALUES (%s, %s, %s, %s)"
            val = (int(userid), name, title, int(companyid))
            cur.execute(sql, val)
            sql = "select jobid from Jobs where title = %s and companyid = %s and name = %s"
            cur.execute(sql, (title, companyid, name))
            jobid = cur.fetchall()[0]['jobid']



        sql = "INSERT INTO Applications (jobid, userid, name, status, application_date) VALUES (%s, %s, %s, %s, %s)"
        val = (int(jobid), int(userid), name, status, datetime.date(appdt.year,appdt.month,appdt.day))
   
        cur.execute(sql, val)


        mydb.commit()
        cur.close()
        mydb.close()

    else: return "Company not found 404", 404


    return True


def getTableContacts(userid):
    mydb = mysql.connector.connect(**config)
    cur = mydb.cursor(dictionary=True)

    sql = "SELECT a.contactid, b.company, b.companyid, a.name as contact, a.email, a.phone, c.jobCount FROM Contacts a LEFT JOIN Companies b ON a.companyid = b.companyid " +\
          "LEFT JOIN (SELECT count(*) as jobcount, companyid, userid FROM Jobs GROUP BY companyid, userid) c " +\
          "ON a.companyid = c.companyid and a.userid = c.userid WHERE a.userid = %s " 

    cur.execute(sql, (userid,))

    vals = cur.fetchall()

    mydb.close()
    return(vals)

def getUserForMock():
    mydb = mysql.connector.connect(**config)
    cur = mydb.cursor(dictionary=True)

    sql = "select userid from Users"
    cur.execute(sql)
    val = cur.fetchone()
    userid = int(val['userid'])

    mydb.close()
    return userid

def getTableCompanies(userid):
    mydb = mysql.connector.connect(**config)
    cur = mydb.cursor(dictionary=True)

    sql = """SELECT Companies.companyid, Companies.company, Jobs.title, Jobs.jobid, Contacts.name
            FROM Jobs
            INNER JOIN Companies ON Jobs.companyid = Companies.companyid
            LEFT JOIN Contacts ON Companies.companyid = Contacts.companyid
            WHERE Jobs.userid = %s;"""
            # ORDER BY Companies.company;"""

    cur.execute(sql, (userid,))

    vals = cur.fetchall()
    print("TABLE COMPANIES", vals)

    mydb.close()
    return(vals)

def addCompany(company_attributes, userid):
    mydb = mysql.connector.connect(**config)
    cur = mydb.cursor(dictionary=True)

    company = company_attributes["company"]
    title = company_attributes["title"]
    name = 'We Should Get Rid Of This'

    check_company_name = "SELECT * FROM Companies"
    cur.execute(check_company_name)
    check_name = cur.fetchall()

    # Check for duplicate company name
    for i in check_name:
        same_company_id = ''
        if (i['company']) == company:
            same_company_id = i['companyid']
            # print("SAME ID", same_company_id, company)
            sql2 = "INSERT INTO Jobs (userid, name, title, companyid) VALUES (%s, %s, %s, %s)"
            val2 = (int(userid), name, title, same_company_id)
            cur.execute(sql2, val2)

            mydb.commit()
            cur.close()
            mydb.close()

            return True
            
    # When Company Name is unique
    sql = "INSERT INTO Companies (company) VALUES (%s)"
    val = (company,)
    cur.execute(sql, val)
    mydb.commit()

    getcompanyid = """SELECT Companies.companyid 
                FROM Companies 
                ORDER BY Companies.companyid 
                DESC LIMIT 1;"""
    cur.execute(getcompanyid)
    vals = cur.fetchone()
    companyid = int(vals['companyid'])

    sql2 = "INSERT INTO Jobs (userid, name, title, companyid) VALUES (%s, %s, %s, %s)"
    val2 = (int(userid), name, title, companyid)
    cur.execute(sql2, val2)

    mydb.commit()
    cur.close()
    mydb.close()

    return True

def deleteCompany(company_attributes, userid):
    mydb = mysql.connector.connect(**config)
    cur = mydb.cursor(dictionary=True)
    company_id = int(company_attributes["companyid"])
    job_id = int(company_attributes["jobid"])
    print("COMPANY ID", company_id)
    print("JOB ID", job_id)

    # SOMETHING WEIRD IS HAPPENING WHERE THE DELETE PAGE ISN'T BEING REFRESHED UPON
    # DELETE SOMETIMES. STILL TRYING TO FIGURE THAT OUT. 
    
    sql = "DELETE FROM Jobs WHERE jobid = %s AND companyid = %s AND userid = %s"
    val = (job_id, company_id, userid)
    cur.execute(sql, val)

    sql_2 = "DELETE FROM Applications WHERE jobid = %s AND userid = %s"
    val_2 = (job_id, userid)
    cur.execute(sql_2, val_2)

    mydb.commit()
    cur.close()
    mydb.close()

    return True

# database calls for skills

def getTableSkills(userid):
    mydb = mysql.connector.connect(**config)
    cur = mydb.cursor(dictionary=True)

    sql = "select a.skillid, a.name as skill, a.proficiency as pro, b.jobMatch FROM Skills a LEFT JOIN " +\
          "(SELECT count(*) as jobMatch, skillid from JobsSkills GROUP BY skillid ) b ON a.skillid = b.skillid WHERE a.userid = %s"

    cur.execute(sql, (userid,))

    vals = cur.fetchall()

    mydb.close()
    return(vals)

def addSkill(skill, userid):
    mydb = mysql.connector.connect(**config)
    cur = mydb.cursor(dictionary=True)
    name = skill["name"]
    prof = int(skill['proficiency'])

    sql = "INSERT INTO Skills (userId, name, proficiency) VALUES (%s,%s,%s)"
    val = (userid, name, prof)
    cur.execute(sql, val)


    mydb.commit()
    cur.close()
    mydb.close()

    return True


def addContact(contact, userid):
    mydb = mysql.connector.connect(**config)
    cur = mydb.cursor(dictionary=True)

    name = contact["name"]
    company = contact["company"]

    sql = "select companyid from Companies where company = %s"

    cur.execute(sql, (company,))

    companyid = cur.fetchall()[0]['companyid']

    email = contact["email"]
    phone = contact["phone"]


    sql = "INSERT INTO Contacts (userid, name, companyid, email, phone) VALUES (%s, %s, %s, %s, %s)"
    val = (userid, name, companyid, email, phone)
    cur.execute(sql, val)


    mydb.commit()
    cur.close()
    mydb.close()

    return True

def addApplications(application, userid, curr_date):
    mydb = mysql.connector.connect(**config)
    cur = mydb.cursor(dictionary=True)

    print("date type:" +str(type(curr_date)) + curr_date)

    title = application["title"]
    company = application["company"]
    status = application["status"]

    sql = "select companyid from Companies where company = %s"
    cur.execute(sql, (company,))
    companyid = cur.fetchall()[0]['companyid']

    print("Company id "+str(companyid))

    sql = "select jobid from Jobs where title = %s and companyid = %s"
    cur.execute(sql, (title, companyid))
    jobid = cur.fetchall()[0]['jobid']

    sql = "INSERT INTO Applications (jobid, userid, name, status, application_date) VALUES (%s, %s, %s, %s, %s)"
    val = (int(jobid), int(userid), name, status, datetime.date(appdt.year,appdt.month,appdt.day))
   
    cur.execute(sql, val)


    mydb.commit()
    cur.close()
    mydb.close()

    return True

def updateSkill(skill, userid, skillid):
    mydb = mysql.connector.connect(**config)
    cur = mydb.cursor(dictionary=True)

    name = skill["name"]
    prof = int(skill['proficiency'])

    sql = "UPDATE Skills SET userid = %s, name = %s, proficiency = %s where skillid = %s"
    val = (userid, name, prof, skillid)
    cur.execute(sql, val)


    mydb.commit()
    cur.close()
    mydb.close()

    return True

def updateContact(contact, userid, contactid):
    mydb = mysql.connector.connect(**config)
    cur = mydb.cursor(dictionary=True)

    name = contact["name"]
    #companyid = contact["companyid"]
    email = contact["email"]
    phone = contact["phone"]

    sql = "UPDATE Contacts SET userid = %s, name = %s, email = %s, phone = %s where contactid = %s"
    val = (userid, name, email, phone, contactid)
    cur.execute(sql, val)


    mydb.commit()
    cur.close()
    mydb.close()

    return True

def updateApplications(application, userid, appid):
    mydb = mysql.connector.connect(**config)
    cur = mydb.cursor(dictionary=True)

    title = application["title"]
    company = application["company"]
    name = application["name"]
    status = application["status"]["value"]
    appdt = parser.parse(application["appdt"])
    status = application["status"]

    sql = "select companyid from Companies where company = %s"
    cur.execute(sql, (company,))
    companyid = cur.fetchall()[0]['companyid']

    sql = "select jobid from Jobs where title = %s and companyid = %s and name = %s"
    cur.execute(sql, (title, companyid, name))
    jobid = cur.fetchall()
    
    if len(jobid) > 0:
        jobid = jobid[0]['jobid']
    else:
        sql = "INSERT INTO Jobs (userid, name, title, companyid) VALUES (%s, %s, %s, %s)"
        val = (int(userid), name, title, int(companyid))
        cur.execute(sql, val)
        sql = "select jobid from Jobs where title = %s and companyid = %s and name = %s"
        cur.execute(sql, (title, companyid, name))
        jobid = cur.fetchall()[0]['jobid']


    sql = "UPDATE Applications SET jobid = %s, userid = %s, name = %s, status = %s, application_date = %s where appid = %s"
    val = (int(jobid), int(userid), name, status, datetime.date(appdt.year,appdt.month,appdt.day), int(appid))
    cur.execute(sql, val)


    mydb.commit()
    cur.close()
    mydb.close()

    return True

def deleteSkill(skillid):
    mydb = mysql.connector.connect(**config)
    cur = mydb.cursor(dictionary=True)

    sql = "DELETE FROM Skills WHERE skillid = %s"
    val = (skillid,)
    cur.execute(sql, val)


    mydb.commit()
    cur.close()
    mydb.close()

    return True

def deleteContact(contactid):
    mydb = mysql.connector.connect(**config)
    cur = mydb.cursor(dictionary=True)

    sql = "DELETE FROM Contacts WHERE contactid = %s"
    val = (contactid,)
    cur.execute(sql, val)


    mydb.commit()
    cur.close()
    mydb.close()

    return True
  
def deleteApplications(appid):
    mydb = mysql.connector.connect(**config)
    cur = mydb.cursor(dictionary=True)

    sql = "DELETE FROM Applications WHERE appid = %s"
    val = (appid,)
    cur.execute(sql, val)


    mydb.commit()
    cur.close()
    mydb.close()

    return True
  
# database calls for authentication/login/sign-up

def check_login(user_info):
    mydb = mysql.connector.connect(**config)
    cur = mydb.cursor()
    username = user_info['username']
    password = user_info['password']
    query = "SELECT userid FROM Users WHERE username = %s AND password = %s"
    values = (username, password)
    cur.execute(query, values)
    results = cur.fetchall()
    cur.close()
    mydb.close()
    
    if len(results) == 0:
        return None
    return results[0][0]

def check_username_unique(username):
    mydb = mysql.connector.connect(**config)
    cur = mydb.cursor()
    query = "SELECT COUNT(*) FROM Users WHERE username = %s"
    values = (username, )
    cur.execute(query, values)

    results = cur.fetchall()
    count = int(results[0][0])

    cur.close()
    mydb.close()

    print(count)

    if count > 0:
        return False

    return True

def signup_user(sent_info):
    username = sent_info['username']
    password = sent_info['password']
    email = sent_info['email']

    if not check_username_unique(username):
        return False

    mydb = mysql.connector.connect(**config)
    cur = mydb.cursor()
    query = "INSERT INTO Users (username, password, email) VALUES (%s, %s, %s)"
    values = (username, password, email)
    cur.execute(query, values)
    mydb.commit()
    
    cur.close()
    mydb.close()

    return True

def main():
    createAndSeedTables()

if __name__ == "__main__":
    main()
