import mysql.connector
import os
from dotenv import load_dotenv
import datetime


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

    sql = "CREATE TABLE Companies (companyid INT AUTO_INCREMENT PRIMARY KEY, company VARCHAR(50) NOT NULL)"
    mycursor.execute(sql)

    sql = "CREATE TABLE Jobs (jobid INT AUTO_INCREMENT PRIMARY KEY,\
    userid INT NOT NULL, name VARCHAR(50) NOT NULL, title VARCHAR(50) NOT NULL, companyid INT NOT NULL,\
    FOREIGN KEY(userid) REFERENCES Users(userid), FOREIGN KEY(companyid) REFERENCES Companies(companyid))"
    mycursor.execute(sql)

    sql = "CREATE TABLE Applications (appid INT AUTO_INCREMENT PRIMARY KEY,\
    jobid INT NOT NULL, userid INT NOT NULL, name VARCHAR(50) NOT NULL, status VARCHAR(50) NOT NULL, application_date DATE NOT NULL,\
    FOREIGN KEY(jobid) REFERENCES Jobs(jobid), FOREIGN KEY(userid) REFERENCES Users(userid))"
    mycursor.execute(sql)

    sql = "CREATE TABLE Skills (skillid INT AUTO_INCREMENT PRIMARY KEY,\
    userid INT NOT NULL, name VARCHAR(50) NOT NULL, proficiency VARCHAR(25) NOT NULL,\
    FOREIGN KEY(userid) REFERENCES Users(userid))"
    mycursor.execute(sql)

    sql = "CREATE TABLE JobsSkills (id INT AUTO_INCREMENT PRIMARY KEY,\
    skillid INT NOT NULL, jobid INT NOT NULL, FOREIGN KEY(skillid) REFERENCES Skills(skillid),\
    FOREIGN KEY(jobid) REFERENCES Jobs(jobid))"
    mycursor.execute(sql)

    sql = "CREATE TABLE Contacts (contactid INT AUTO_INCREMENT PRIMARY KEY,\
    userid INT NOT NULL, name VARCHAR(50), companyid INT, email VARCHAR(50), phone VARCHAR(15),\
    FOREIGN KEY(userid) REFERENCES Users(userid), FOREIGN KEY(companyid) REFERENCES Companies(companyid))"
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

    sql = "INSERT INTO Jobs (userid, name, title, companyid) VALUES (%s, %s, %s, %s)"
    val = (int(userid), "A start", "Jr. Software Engineer", int(companyid2))
    mycursor.execute(sql, val)



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

    sql = "SELECT b.title AS title, c.company AS company, a.application_date AS appdt FROM Applications a LEFT JOIN Jobs b ON " + \
          " a.jobid = b.jobid LEFT JOIN Companies c on b.companyid = c.companyid WHERE a.userid = %s"
    
    cur.execute(sql, (userid,))

    vals = cur.fetchall()

    mydb.close()
    return(vals)


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

    sql = "SELECT a.company, b.name as contact, c.count as jobCount FROM Companies a LEFT JOIN Contacts b ON a.companyid = b.companyid " +\
            "AND b.userid = %s LEFT JOIN (SELECT count(*) as count, companyid, userid from Jobs GROUP BY companyid, userid) c "\
            "ON b.companyid = c.companyid AND b.userid = c.userid"


    cur.execute(sql, (userid,))

    vals = cur.fetchall()

    mydb.close()
    return(vals)

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



# database calls for authentication/login/sign-up

def check_login(user_info):
    mydb = mysql.connector.connect(**config)
    cur = mydb.cursor()
    username = user_info['username']
    password = user_info['password']
    print(password)
    query = "SELECT userid FROM Users WHERE username = %s AND password = %s"
    values = (username, password)
    cur.execute(query, values)
    results = cur.fetchall()
    cur.close()
    mydb.close()
    
    if len(results) == 0:
        return None
    return results[0][0]

def main():
    createAndSeedTables()

if __name__ == "__main__":
    main()
