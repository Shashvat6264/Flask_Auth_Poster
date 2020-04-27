# Flask_Auth_Poster
To make an app in Flask which is a post putting platform for users 

## How to run it
1. Start the Virtual environment 
```bash 
source bin/activate
```
2. Change directory to app
```bash 
cd app
```
3. Run
```bash 
export FLASK_APP=app.py
```
then: 
```bash 
export FLASK_DEBUG=1
```
4. Initialize the database. Run:
```bash 
flask db init
```
Then migrate the models:
```bash 
flask db migrate
```
Then upgrade the database type:
```bash 
flask db upgrade
```
5. Now everything in the app is set. To launch the app run:
```bash 
flask run
```
6. Go to the url 
```
127.0.0.1:5000/
``` 
to see the app in action.
