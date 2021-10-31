

#     sql = "CREATE TABLE Applications (appid INT AUTO_INCREMENT PRIMARY KEY,\
#     jobid INT NOT NULL, userid INT NOT NULL, name VARCHAR(50) NOT NULL, status VARCHAR(50) NOT NULL, application_date DATE NOT NULL,\
#     FOREIGN KEY(jobid) REFERENCES Jobs(jobid), FOREIGN KEY(userid) REFERENCES Users(userid))"
#     mycursor.execute(sql)



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
    
    mycursor.execute("DROP TABLE IF EXISTS Applications")
    mycursor.execute("DROP TABLE IF EXISTS Contacts")
    mycursor.execute("DROP TABLE IF EXISTS JobsCompany")
    mycursor.execute("DROP TABLE IF EXISTS JobsSkills")
    mycursor.execute("DROP TABLE IF EXISTS Jobs")
    mycursor.execute("DROP TABLE IF EXISTS Companies")
    mycursor.execute("DROP TABLE IF EXISTS Skills")
    mycursor.execute("DROP TABLE IF EXISTS Users")
    

    # create tables
    sql = "CREATE TABLE Users (userid INT AUTO_INCREMENT PRIMARY KEY,\
    username VARCHAR(50) NOT NULL, password VARCHAR(25) NOT NULL, email VARCHAR(50) NOT NULL)"
    mycursor.execute(sql)

    
    sql = "CREATE TABLE Skills (skillid INT AUTO_INCREMENT PRIMARY KEY,\
    userid INT NOT NULL, name VARCHAR(50) NOT NULL, proficiency VARCHAR(25) NOT NULL,\
    FOREIGN KEY(userid) REFERENCES Users(userid))"
    mycursor.execute(sql)

    sql = "CREATE TABLE Companies (companyid INT AUTO_INCREMENT PRIMARY KEY,\
    userid INT NOT NULL, name VARCHAR(100) NOT NULL, contacts VARCHAR(100) NOT NULL,\
    FOREIGN KEY(userid) REFERENCES Users(userid))"
    mycursor.execute(sql)

    sql = "CREATE TABLE Jobs (jobid INT AUTO_INCREMENT PRIMARY KEY,\
    userid INT NOT NULL, name VARCHAR(50) NOT NULL, title VARCHAR(50) NOT NULL, companyid INT NOT NULL,\
    FOREIGN KEY(userid) REFERENCES Users(userid), FOREIGN KEY(companyid) REFERENCES Companies(companyid))"
    mycursor.execute(sql)

    sql = "CREATE TABLE JobsSkills (id INT AUTO_INCREMENT PRIMARY KEY,\
    skillid INT NOT NULL, jobid INT NOT NULL, FOREIGN KEY(skillid) REFERENCES Skills(skillid),\
    FOREIGN KEY(jobid) REFERENCES Jobs(jobid))"
    mycursor.execute(sql)

    sql = "CREATE TABLE Applications (appid INT AUTO_INCREMENT PRIMARY KEY,\
    jobid INT NOT NULL, userid INT NOT NULL, name VARCHAR(50) NOT NULL, status VARCHAR(50) NOT NULL, application_date DATE NOT NULL,\
    FOREIGN KEY(jobid) REFERENCES Jobs(jobid), FOREIGN KEY(userid) REFERENCES Users(userid))"
    mycursor.execute(sql)

    sql = "CREATE TABLE JobsCompany (id INT AUTO_INCREMENT PRIMARY KEY,\
    companyid INT NOT NULL, jobid INT NOT NULL, FOREIGN KEY(companyid) REFERENCES Companies(companyid),\
    FOREIGN KEY(jobid) REFERENCES Jobs(jobid))"
    mycursor.execute(sql)

    sql = "CREATE TABLE Contacts (contactid INT AUTO_INCREMENT PRIMARY KEY,\
    userid INT NOT NULL, name VARCHAR(50), companyid INT, email VARCHAR(50), phone VARCHAR(15),\
    FOREIGN KEY(userid) REFERENCES Users(userid), FOREIGN KEY(companyid) REFERENCES Companies(companyid))"
    mycursor.execute(sql)

    mydb.commit()
    mycursor.close()

    mycursor = mydb.cursor()

    # seed tables with dummy data
    sql = "INSERT INTO Users (username, password, email) VALUES (%s, %s, %s)"
    val = ("someuser", 12345, "someuser@test.com")
    mycursor.execute(sql, val)

    sql = "select userid from users"
    mycursor.execute(sql)
    val = mycursor.fetchone()
    userid = val[0]
    
    sql = "INSERT INTO Skills (userid, name, proficiency) VALUES (%s, %s, %s)"
    val = (int(userid), "Javascript", "2")
    mycursor.execute(sql, val)

    sql = "INSERT INTO Companies (userid, name, contacts) VALUES (%s, %s, %s)"
    val = (int(userid), "FAANGERMMAIGAWD", "Elizabeth Holmes")
    mycursor.execute(sql, val)

    sql = "select companyid from companies"
    mycursor.execute(sql)
    val = mycursor.fetchone()
    companyid = val[0]
    # while val:
    #     companyid = val[0]
    #     val = mycursor.fetchone()

    sql = "INSERT INTO Jobs (userid, name, title, companyid) VALUES (%s, %s, %s, %s)"
    val = (int(userid), "Hope I get it", "Software Engineer I", int(companyid))
    mycursor.execute(sql, val)

    sql = "select jobid from jobs"
    mycursor.execute(sql)
    val = mycursor.fetchone()
    jobid = val[0]

    sql = "INSERT INTO JobsCompany (companyid, jobid) VALUES (%s, %s)"
    val = (int(companyid), int(jobid))
    mycursor.execute(sql, val)

    # sql = "INSERT INTO Applications (jobid, userid, name, status, application_date) VALUES (%s, %s, %s, %s, %s)"
    # val = (int(jobid), int(userid), "First Application", "Applied", datetime.date(2021,10,1))
    # mycursor.execute(sql, val)

    sql = "select skillid from skills"
    mycursor.execute(sql)
    val = mycursor.fetchone()
    skillid = val[0]

    sql = "INSERT INTO JobsSkills (skillid, jobid) VALUES (%s, %s)"
    val = (int(skillid), int(jobid))
    mycursor.execute(sql, val)

    sql = "INSERT INTO Contacts (userid, name, companyid, email, phone) VALUES (%s, %s, %s, %s, %s)"
    val = (int(userid), 'John Doe', int(companyid), 'jdoe@gfaangermaigawd.com', '555-555-5555')
    mycursor.execute(sql, val)


    mydb.commit()
    mycursor.close()
    mydb.close()


def getTableApplications(userid):
    mydb = mysql.connector.connect(**config)
    cur = mydb.cursor(dictionary=True)

    sql = "SELECT b.title AS title, c.company AS company, a.application_date AS appdt FROM Applications a LEFT JOIN Jobs b ON " + \
          "a.userid = b.userid AND a.jobid = b.jobid LEFT JOIN Companies c on b.companyid = c.companyid WHERE a.userid = %s"
    
    cur.execute(sql, (userid,))

    vals = cur.fetchall()

    mydb.close()
    return(vals)


def getTableContacts(userid):
    mydb = mysql.connector.connect(**config)
    cur = mydb.cursor(dictionary=True)

    sql = "SELECT b.company, a.name as contact, c.jobCount FROM Contacts a LEFT JOIN Companies b ON a.companyid = b.companyid " +\
          "LEFT JOIN (SELECT count(*) as jobcount, companyid, userid FROM Jobs GROUP BY companyid, userid) c " +\
          "ON a.companyid = c.companyid and a.userid = c.userid WHERE a.userid = %s " 

    cur.execute(sql, (userid,))

    vals = cur.fetchall()

    mydb.close()
    return(vals)

def getTableSkills(userid):
    mydb = mysql.connector.connect(**config)
    cur = mydb.cursor(dictionary=True)

    sql = "select a.skillid, a.name as skill, a.proficiency as pro, b.jobMatch FROM Skills a LEFT JOIN " +\
          "(SELECT count(*) as jobMatch, skillid from JobsSkills GROUP BY skillid ) b ON a.skillid = b.skillid WHERE a.userid = %s"

    cur.execute(sql, (userid,))

    vals = cur.fetchall()

    mydb.close()
    return(vals)

def getTableCompanies(userid):
    mydb = mysql.connector.connect(**config)
    cur = mydb.cursor(dictionary=True)

    sql = "select a.companyid, a.name as company, a.contacts as cont, b.jobMatch FROM Companies a LEFT JOIN " +\
          "(SELECT count(*) as jobMatch, companyid from JobsCompany GROUP BY companyid ) b ON a.companyid = b.companyid WHERE a.userid = %s"

    cur.execute(sql, (userid,))

    vals = cur.fetchall()

    mydb.close()
    return(vals)

def getUserForMock():
    mydb = mysql.connector.connect(**config)
    cur = mydb.cursor(dictionary=True)

    sql = "select userid from users"
    cur.execute(sql)
    val = cur.fetchone()
    userid = int(val['userid'])

    mydb.close()
    return userid

def addSkill(skill, userid):
    mydb = mysql.connector.connect(**config)
    cur = mydb.cursor(dictionary=True)
    name = skill["name"]
    prof = int(skill['proficiency'])

    sql = "INSERT INTO skills (userId, name, proficiency) VALUES (%s,%s,%s)"
    val = (userid, name, prof)
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

    sql = "UPDATE skills SET userid = %s, name = %s, proficiency = %s where skillid = %s"
    val = (userid, name, prof, skillid)
    cur.execute(sql, val)


    mydb.commit()
    cur.close()
    mydb.close()

    return True

def deleteSkill(skillid):
    mydb = mysql.connector.connect(**config)
    cur = mydb.cursor(dictionary=True)

    sql = "DELETE FROM skills WHERE skillid = %s"
    val = (skillid,)
    cur.execute(sql, val)


    mydb.commit()
    cur.close()
    mydb.close()

    return True

def addCompany(company, userid):
    mydb = mysql.connector.connect(**config)
    cur = mydb.cursor(dictionary=True)
    name = company["name"]
    contact = company["contacts"]

    sql = "INSERT INTO companies (userid, name, contacts) VALUES (%s,%s,%s)"
    val = (userid, name, contact)
    cur.execute(sql, val)


    mydb.commit()
    cur.close()
    mydb.close()

    return True

def updateCompany(company, userid, companyid):
    mydb = mysql.connector.connect(**config)
    cur = mydb.cursor(dictionary=True)

    name = company["name"]
    contact = company["contacts"]

    sql = "UPDATE companies SET userid = %s, name = %s, contacts = %s where companyid = %s"
    val = (userid, name, contact, companyid)
    cur.execute(sql, val)


    mydb.commit()
    cur.close()
    mydb.close()

    return True

def deleteCompany(companyid):
    mydb = mysql.connector.connect(**config)
    cur = mydb.cursor(dictionary=True)

    sql = "DELETE FROM companies WHERE companyid = %s"
    val = (companyid,)
    cur.execute(sql, val)


    mydb.commit()
    cur.close()
    mydb.close()

    return True


def main():
    createAndSeedTables()

if __name__ == "__main__":
    main()