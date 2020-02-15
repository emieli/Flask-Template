
# Flask Template
This is a project setup to help beginners get started with Flask. The goal is provide a sample website that show how Flask can be used to build a website following current best practices (to the best of my knowledge).
## What the website does
- The main part of the website shows a simple "Hello world!" type message.
- The blog part of the website show you how you can dynamically build webpages.
- By using Flask blueprints, code for the two parts of the website are separated.
- The website is made pretty using Bootstrap, you can find more info about it here: https://getbootstrap.com/
## How to install
This guide assumes you have sudo access to a Debian 10 machine. Commands may otherwise be different.
### 1. Make sure Debian has the required dependencies
    sudo apt update
    sudo apt install git python3-pip python3-venv

We use git to clone this repo to a local folder on your device. Pip is used to download the required python modules. And we run the flask server in a python virtualenv to keep it separate from other projects on the same machine.

### 2. Clone the repo and enter the folder
	user@server:~$ git clone https://github.com/emileliason/Flask-Template.git
	Cloning into 'Flask-Template'...
	Unpacking objects: 100% (24/24), done.
	user@server:~$ cd Flask-Template/
### 3. Build and enter the Virtualenv
	user@server:~/Flask-Template$ python3 -m venv venv
	user@server:~/Flask-Template$ source venv/bin/activate
	(venv) user@server:~/Flask-Template$ 
### 4. Install the required python modules
	(venv) user@server:~/Flask-Template$ pip install -r pip-requirements.txt
	Successfully installed Jinja2-2.11.1 MarkupSafe-1.1.1 Werkzeug-1.0.0 certifi-2019.11.28 chardet-3.0.4 click-7.0 flask-1.1.1 idna-2.8 itsdangerous-1.1.0 requests-2.22.0 urllib3-1.25.8
### 5. Start the flask server in development mode
	(venv) user@server:~/Flask-Template$ export FLASK_ENV=development
	(venv) user@server:~/Flask-Template$ flask run --host=0.0.0.0
	 * Environment: development
	 * Debug mode: on
	 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
	 * Restarting with stat
	 * Debugger is active!
	 * Debugger PIN: 136-119-655
### 6. All done! 
You should now be able to use your browser on the local or a nearby device to reach the webpage on port 5000.
http://\<your-debian-ip\>:5000

	
	
    

