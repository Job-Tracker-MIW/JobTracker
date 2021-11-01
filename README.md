# JobTracker
Job Tracker web application

# Install:
1. python3 (latest version)
2. npm
3. NodeJS
4. Create a virtual environment for local development of Flask
Walkthrough for installing virtual env and Flask https://www.section.io/engineering-education/complete-guide-on-installing-flask-for-beginners/
5. Flask
6. npm install react-router-dom
7. npm install --save styled-components
8. npm install react-icons --save
9. npm install react-minimal-side-navigation
10. npm install react-scripts
10. Might need to 'pip3 install dotenv' and 'pip3 install mysql-connector'
    - If having issues, use pip3 install python-dotenv instead
12. npm install react-bootstrap bootstrap@5.1.3

Note: Execute 'source env/bin/activate' before working with Flask to work in virtual env

Note 2: make sure your virtual environment is in the root folder named 'env' so it is ignored by git

# How To Run Frontend Only:
1. Navigate to ./client folder
2. Execute 'npm start'

# How To Run Backend
1. Navigate to root folder
2. Execute 'flask run' or 'python3 app.py'


# How To Compile and Run Entire app (how app will run in production):
1. Navigate to ./client folder
2. Execute 'npm run build' (this will create a build folder with static files)
3. Execute 'flask run' or 'python3 app.py' from root folder

# Steps to get MySQL working and connected to application
MAC OS
1.	Pull latest from Github
2.	Install MySQL Community Server here: https://dev.mysql.com/downloads/mysql/ on Linux do not use sudo apt install mysql-server 
         instead use wget https://dev.mysql.com/get/mysql-apt-config_0.8.19-1_all.deb  then sudo apt install ./mysql-apt-config_0.8.19-1_all.deb 
3.	IMPORTANT: Set Authentication method to legacy during installation (do not choose default)
4.	Set a default root password during install (save this password somewhere)
5.	Open Terminal
6.	Create shortcut: sudo sh -c 'echo /usr/local/mysql/bin > /etc/paths.d/mysql'
7.	Connect: mysql -u root -p (Should show MySQL info if connected)
8.	Create db: CREATE DATABASE jobtracker;
9.	Select DB: USE jobtracker
10.	Show all tables in DB: show tables; (should show 0 for now)
11.	Navigate to project folder in terminal or terminal in IDE with project open (Ex. VSCode)
12.	Install MySQL: pip3 install mysql-connector
13.	Install DotEnv: pip3 install dotenv 

    a.	This allows you to use environment variables to store local MySQL connection creds

14.	Create a ‘.env’ file in the root of the project folder and add database credentials

DB_HOST="localhost" <br />
DB_USER="root" <br />
DB_PASSWORD="" <br />
DB_DATABASE="jobtracker" <br />
DB_CREATE_SEED=True <br />

15.	Make sure .env is in the .gitignore file so it isn’t pushed to our repo
16.	Run app.py


Note: DB_CREATE_SEED should be set to True if you want to recreate table and seed with dummy data


UBUNTU 20.04
1. if needed may need to uninstall older version first 
   - Remove mysql - https://www.digitalocean.com/community/questions/completely-uninstall-mysql-server
   - sudo apt remove --purge mysql-server
   - sudo apt purge mysql-server
   - sudo apt autoremove
   - sudo apt autoclean
   - sudo apt remove dbconfig-mysql

2. install my sql 
   - sudo apt update
   - sudo apt install mysql-server

3. IMPORTANT: Set Authentication method to legacy during installation (do not choose default)

4. edit /etc/mysql/my.cnf
   insert in [mysqld] (create it doesn't exist)
   lower_case_table_names = 1

5. Set a default root password during install (save this password somewhere)

6. create the shortcut 
   - sudo service mysql stop
   - sudo usermod -d /var/lib/mysql/ mysql
   - sudo service mysql start

   if service fails to start try:
   - sudo apt-get purge mysql-server mysql-client mysql-common
   - sudo apt-get install mysql-server

7. Open Terminal

8. Connect: mysql -u root -p (Should show MySQL info if connected)
   If you get an authentication error run:
   - sudo mysql -u root
   - ALTER USER 'root'@'localhost' IDENTIFIED BY 'MyNewPass';
   then mysql -u root -p
   - save the password
9. Create db: CREATE DATABASE jobtracker;

10. Select DB: USE jobtracker

11. Show all tables in DB: show tables; (should show 0 for now)

12. Navigate to project folder in terminal or terminal in IDE with project open (Ex. VSCode)

13. Install MySQL: pip3 install mysql-connector or may need pip3 install mysql-connector-python 

14. Install DotEnv: pip3 install dotenv or may need pip3 install dotenv-python

    a. This allows you to use environment variables to store local MySQL connection creds

15. Create a ‘.env’ file in the root of the project folder and add database credentials

DB_HOST="localhost"
DB_USER="root"
DB_PASSWORD=""
DB_DATABASE="jobtracker"
DB_CREATE_SEED=True

16. Make sure .env is in the .gitignore file so it isn’t pushed to our repo
17. Run app.py

# Install Python dependencies
1. Execute "pip3 install -r requirements.txt" from root folder of project

# Run Database standup script on Heroku
1. heroku login
2. heroku run python database/database_config.py -a job-tracker-matt-isaac-wil


