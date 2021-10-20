import mysql.connector
import os
from dotenv import load_dotenv
import datetime

load_dotenv()

mydb = mysql.connector.connect(
  host=os.environ["DB_HOST"],
  user=os.environ["DB_USER"],
  password=os.environ["DB_PASSWORD"],
  database=os.environ["DB_DATABASE"]
)

def createTables():
    mycursor = mydb.cursor()

    # drop tables
    mycursor.execute("DROP TABLE IF EXISTS JobsSkills")
    mycursor.execute("DROP TABLE IF EXISTS Applications")
    mycursor.execute("DROP TABLE IF EXISTS Skills")
    mycursor.execute("DROP TABLE IF EXISTS Jobs")
    mycursor.execute("DROP TABLE IF EXISTS Users")

    # create tables
    sql = "CREATE TABLE Users (userid INT AUTO_INCREMENT PRIMARY KEY,\
    username VARCHAR(50) NOT NULL, password VARCHAR(25) NOT NULL, email VARCHAR(50) NOT NULL)"
    mycursor.execute(sql)

    sql = "CREATE TABLE Jobs (jobid INT AUTO_INCREMENT PRIMARY KEY,\
    userid INT NOT NULL, name VARCHAR(50) NOT NULL, title VARCHAR(50) NOT NULL, company VARCHAR(50) NOT NULL,\
    FOREIGN KEY(userid) REFERENCES Users(userid))"
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

    mydb.commit()
    mycursor.close()


def seedTables():
    mycursor = mydb.cursor()

    # seed tables with dummy data
    sql = "INSERT INTO Users (username, password, email) VALUES (%s, %s, %s)"
    val = ("someuser", 12345, "someuser@test.com")
    mycursor.execute(sql, val)

    sql = "INSERT INTO Skills (userid, name, proficiency) VALUES (%s, %s, %s)"
    val = (1, "Javascript", "Not Great")
    mycursor.execute(sql, val)

    sql = "INSERT INTO Jobs (userid, name, title, company) VALUES (%s, %s, %s, %s)"
    val = (1, "Hope I get it", "Software Engineer I", "FAANGERMMAIGAWD")
    mycursor.execute(sql, val)

    sql = "INSERT INTO Applications (jobid, userid, name, status, application_date) VALUES (%s, %s, %s, %s, %s)"
    val = (1, 1, "First Application", "Applied", datetime.date(2021,10,1))
    mycursor.execute(sql, val)

    sql = "INSERT INTO JobsSkills (skillid, jobid) VALUES (%s, %s)"
    val = (1, 1)
    mycursor.execute(sql, val)

    mydb.commit()
    mycursor.close()
    mydb.close()


def main():
    createTables()
    seedTables()

if __name__ == "__main__":
    main()