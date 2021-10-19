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

# Install and setup database
1. Install MySQL Community Server https://dev.mysql.com/downloads/mysql/
2. Connect with terminal: mysql -u root -p
3. Create db: CREATE DATABASE jobtracker;
4. Select DB: USE jobtracker;
5. Create a ‘.env’ file in the root of the project folder and add the following:

DB_HOST="localhost"
DB_USER="root"
DB_PASSWORD=""
DB_DATABASE="bookswap" 
DB_CREATE_SEED=False

Note: DB_CREATE_SEED should be set to True if you want to recreate table and seed with dummy data

