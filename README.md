# JobTracker
Job Tracker web application

Install:
1. python3 (latest version)
2. npm
3. NodeJS
4. Create a virtual environment for local development of Flask
Walkthrough for installing virtual env and Flask https://www.section.io/engineering-education/complete-guide-on-installing-flask-for-beginners/
5. Flask

Note: Execute 'source env/bin/activate' before working with Flask to work in virtual env

Note 2: make sure your virtual environment is in the root folder named 'env' so it is ignored by git

How To Run Frontend Only:
1. Navigate to ./client folder
2. Execute 'npm start'

How To Run Backend
1. Navigate to root folder
2. Execute 'flask run' or 'python3 app.py'


How To Compile and Run Entire app (how app will run in production):
1. Navigate to ./client folder
2. Execute 'npm run build' (this will create a build folder with static files)
3. Execute 'flask run' or 'python3 app.py' from root folder
