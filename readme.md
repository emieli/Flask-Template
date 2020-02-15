##

Installation:
Debian 10:
sudo apt update
sudo apt install python3-pip python3-venv
cd /opt/flask_app
python3 -m venv venv
pip --version (should show python3.7 or higher, we don't want to use python2)
pip install -r pip-requirements.txt
export FLASK_ENV=development (Will automatically reload the flask server every time a change is made to any of the files.)
flask run --host=0.0.0.0