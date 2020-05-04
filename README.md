
## Receiver for WiFi security camera FTP event triggers 

Docker Container to receive movement images from a WiFi Security Camera over FTP and publish on MQTT

### Standalone Python script

To begin, assuming you have virtualenv installed:
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```
And close the virtualenv using:
```
deactivate
```

or if you want to run without a virtual environment
```
pip install -r requirements.txt
python main.py
```
