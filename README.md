# JobTracker
Job Tracker web application

# Install:
1. python3 (latest version)
2. npm
3. NodeJS
4. Create a virtual environment for local development of Flask
Walkthrough for installing virtual env and Flask https://www.section.io/engineering-education/complete-guide-on-installing-flask-for-beginners/
5. Flask
6. npm install react-route-dom
7. npm install --save styled-components
8. npm install react-icons --save
9. npm install react-minimal-side-navigation
10. Might need to 'pip3 install dotenv' and 'pip3 install mysql-connector'
    - If having issues, use pip3 install python-dotenv instead
11. npm install react-bootstrap bootstrap@5.1.3

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

# Install Python dependencies
1. Execute "pip3 install -r requirements.txt" from root folder of project

# Steps to get MySQL working and connected to application

1.	Pull latest from Github
2.	Install MySQL Community Server here: https://dev.mysql.com/downloads/mysql/
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

