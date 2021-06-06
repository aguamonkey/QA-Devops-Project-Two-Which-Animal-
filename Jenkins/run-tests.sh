sudo apt update 
sudo apt install python3 python3-pip python3-venv -y 

#set up virtual environment
python3 -m venv venv
source venv/bin/activate

#Install pytest
pip3 install -r service1/requirements.txt

# run pytest will need for loop at some point
python3 -m pytest service1 --junitxml=junit/test-results.xml --cov=application --cov-report=xml --cov-report=html --cov-report term-missing
python3 -m pytest service2 --junitxml=junit/test-results.xml --cov=application --cov-report=xml --cov-report=html --cov-report term-missing
python3 -m pytest service3 --junitxml=junit/test-results.xml --cov=application --cov-report=xml --cov-report=html --cov-report term-missing
python3 -m pytest service4 --junitxml=junit/test-results.xml --cov=application --cov-report=xml --cov-report=html --cov-report term-missing
