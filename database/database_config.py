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
    userid INT NOT NULL, name VARCHAR(50) NOT NULL, title VARCHAR(50) NOT NULL, job_status VARCHAR(50), skill VARCHAR(25) NOT NULL, companyid INT NOT NULL, CONSTRAINT job_name UNIQUE (companyid, title, name),\
    FOREIGN KEY(userid) REFERENCES Users(userid) ON DELETE CASCADE, FOREIGN KEY(companyid) REFERENCES Companies(companyid) ON DELETE CASCADE)"
    mycursor.execute(sql)

    # sql = "CREATE TABLE Applications (appid INT AUTO_INCREMENT PRIMARY KEY,\
    # jobid INT NOT NULL, userid INT NOT NULL, name VARCHAR(50) NOT NULL, status VARCHAR(50) NOT NULL, application_date DATE NOT NULL,\
    # FOREIGN KEY(jobid) REFERENCES Jobs(jobid) ON DELETE CASCADE, FOREIGN KEY(userid) REFERENCES Users(userid) ON DELETE CASCADE)"
    # mycursor.execute(sql)

    sql = "CREATE TABLE Applications (appid INT AUTO_INCREMENT PRIMARY KEY,\
    jobid INT NOT NULL, userid INT NOT NULL, name VARCHAR(50) NOT NULL, status VARCHAR(50) NOT NULL, application_date VARCHAR(50) NOT NULL,\
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



    sql = "INSERT INTO Jobs (userid, name, title, skill, companyid, job_status) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (int(userid), "Hope I get it", "Software Engineer I", "Javascript", int(companyid), 'Not Applied')
    mycursor.execute(sql, val)

    sql = "INSERT INTO Jobs (userid, name, title, skill, companyid, job_status) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (int(userid), "looks good!", "Software Engineer II", "C", int(companyid2), 'Not Applied')
    mycursor.execute(sql, val)

    sql = "select jobid from Jobs"
    mycursor.execute(sql)
    val = mycursor.fetchone()
    val2 = mycursor.fetchone()
    jobid = val[0]
    jobid2 = val2[0]

    # APPLICTIONS SHOULD UPDATE WHEN "APPLIED" IS HIT ON JOBS PAGE. FEEL FREE TO DELETE THE INSERT IF APPROVED

    # sql = "INSERT INTO Applications (jobid, userid, name, status, application_date) VALUES (%s, %s, %s, %s, %s)"
    # # val = (int(jobid), int(userid), "First Application", "Applied", datetime.date(2021,10,1))
    # val = (int(jobid), int(userid), "First Application", "Applied", '11/01/21')
    # mycursor.execute(sql, val)

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

    sql = """SELECT Applications.appid, Jobs.title, Companies.company, Jobs.name AS name, Applications.application_date AS appdt, Applications.status
		FROM Applications
		INNER JOIN Jobs ON Applications.jobid = Jobs.jobid
		INNER JOIN Companies ON Jobs.companyid = Companies.companyid
		LEFT JOIN Contacts ON Companies.companyid = Contacts.companyid
		WHERE Jobs.userid = %s;
    """
    
    cur.execute(sql, (userid,))

    jobs = cur.fetchall()

    sql = """SELECT DISTINCT c.company
            FROM Jobs
            INNER JOIN Companies as c ON Jobs.companyid = c.companyid
            WHERE Jobs.userid = %s;"""

    cur.execute(sql, (userid,))

    companies = cur.fetchall()

    companyList = []
    for c in companies:
        companyList.append(c["company"])

    for job in jobs:
        job["companies"] = companyList

    mydb.close()
    return(jobs)

def addToApplied(userid, application, curr_datetime):

    mydb = mysql.connector.connect(**config)
    cur = mydb.cursor(dictionary=True)

    title = application["title"]
    company = application["company"]
    name = application["userDefName"]
    
    if 'status' in application.keys():
        status = application["status"]
    else: status = 'Applied'
    #appdt = curr_datetime #parser.parse(application["appdt"])
    # appdt = parser.parse(curr_datetime)
    appdt = (curr_datetime)

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
        # val = (int(jobid), int(userid), name, status, datetime.date(appdt.year,appdt.month,appdt.day))
        val = (int(jobid), int(userid), name, status, curr_datetime)
   
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

    sql = """SELECT Companies.companyid, Companies.company, Jobs.title, Jobs.skill, Jobs.jobid, Jobs.name as userDefName, Contacts.name
            FROM Jobs
            INNER JOIN Companies ON Jobs.companyid = Companies.companyid
            LEFT JOIN Contacts ON Companies.companyid = Contacts.companyid
            WHERE Jobs.job_status = 'Not Applied' AND Jobs.userid = %s
    """

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
    userDefName = company_attributes["userDefName"]

    skill = company_attributes["skill"]

    check_company_name = "SELECT * FROM Companies"
    cur.execute(check_company_name)
    check_name = cur.fetchall()

    # Check for duplicate company name
    for i in check_name:
        same_company_id = ''
        if (i['company']) == company:
            same_company_id = i['companyid']
            job_status = 'Not Applied'
            # print("SAME ID", same_company_id, company)
            sql2 = "INSERT INTO Jobs (userid, name, title, skill, companyid, job_status) VALUES (%s, %s, %s, %s, %s, %s)"
            val2 = (int(userid), userDefName, title, skill, same_company_id, job_status)
            cur.execute(sql2, val2)
            mydb.commit()

            # check for matching skill and add to JobsSkills if so
            sql = "SELECT skillid FROM Skills where name = %s"
            val = (skill,)
            cur.execute(sql,val)
            skillMatches = cur.fetchall()
            if len(skillMatches) > 0:
                skillMatch = skillMatches[0]["skillid"]

            sql = "SELECT jobid FROM Jobs where Jobs.skill = %s"
            val = (skill,)
            cur.execute(sql,val)
            jobMatches = cur.fetchall()
            if len(jobMatches) > 0:
                jobMatch = jobMatches[0]["jobid"]
            
            if len(jobMatches) > 0 and len(skillMatches) > 0:
                sql = "INSERT INTO JobsSkills (skillid, jobid) VALUES (%s, %s)"
                vals = (int(skillMatch), int(jobMatch))
                cur.execute(sql, vals)
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

    job_status = 'Not Applied'

    sql2 = "INSERT INTO Jobs (userid, name, title, skill, companyid, job_status) VALUES (%s, %s, %s, %s, %s, %s)"
    val2 = (int(userid), userDefName, title, skill, companyid, job_status)
    cur.execute(sql2, val2)
    mydb.commit()

    # check for matching skill and add to JobsSkills if so
    sql = "SELECT skillid FROM Skills where name = %s"
    val = (skill,)
    cur.execute(sql,val)
    skillMatches = cur.fetchall()
    if len(skillMatches) > 0:
        skillMatch = skillMatches[0]["skillid"]

    sql = "SELECT jobid FROM Jobs where jobs.skill = %s"
    val = (skill,)
    cur.execute(sql,val)
    jobMatches = cur.fetchall()
    if len(jobMatches) > 0:
        jobMatch = jobMatches[0]["jobid"]
    
    if len(jobMatches) > 0 and len(skillMatches) > 0:
        sql = "INSERT INTO JobsSkills (skillid, jobid) VALUES (%s, %s)"
        vals = (int(skillMatch), int(jobMatch))
        cur.execute(sql, vals)
        mydb.commit()

    cur.close()
    mydb.close()

    return True

def deleteCompany(company_attributes, userid):
    mydb = mysql.connector.connect(**config)
    cur = mydb.cursor(dictionary=True)
    company_id = int(company_attributes["companyid"])
    job_id = int(company_attributes["jobid"])
    userDefName = company_attributes["userDefName"]
    print("COMPANY ID", company_id)
    print("JOB ID", job_id)

    # SOMETHING WEIRD IS HAPPENING WHERE THE DELETE PAGE ISN'T BEING REFRESHED UPON
    # DELETE SOMETIMES. STILL TRYING TO FIGURE THAT OUT. 
    
    sql = "DELETE FROM Jobs WHERE jobid = %s AND companyid = %s AND userid = %s and name = %s"
    val = (job_id, company_id, userid, userDefName)
    cur.execute(sql, val)

    sql = "DELETE FROM JobsSkills WHERE jobid = %s"
    val = (job_id,)
    cur.execute(sql, val)

    sql_2 = "DELETE FROM Applications WHERE jobid = %s AND userid = %s"
    val_2 = (job_id, userid)
    cur.execute(sql_2, val_2)

    mydb.commit()
    cur.close()
    mydb.close()

    return True

def updateJobApplied(userid, applied_attributes):
    mydb = mysql.connector.connect(**config)
    cur = mydb.cursor(dictionary=True)

    job_id = applied_attributes["jobid"]
    print("JOB ID", job_id)

    set_as_applied = 'Applied'

    sql = "UPDATE Jobs SET job_status = %s WHERE jobid = %s"
    val = (set_as_applied, job_id)

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

    #isaac added
    name = application["name"]
    status = application["status"]

    sql = "select companyid from Companies where company = %s"
    cur.execute(sql, (company,))
    companyid = cur.fetchall()[0]['companyid']

    print("Company id "+str(companyid))

    sql = "select jobid from Jobs where title = %s and companyid = %s"
    cur.execute(sql, (title, companyid))
    jobid = cur.fetchall()[0]['jobid']

    sql = "INSERT INTO Applications (jobid, userid, name, status, application_date) VALUES (%s, %s, %s, %s, %s)"
    # val = (int(jobid), int(userid), name, status, datetime.date(appdt.year,appdt.month,appdt.day))
    val = (int(jobid), int(userid), name, status, curr_date)
   
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

    print(application)

    title = application["title"]
    company = application["company"]["value"]
    name = application["name"]
    status = application["status"]
    appdt = parser.parse(application["appdt"])

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
