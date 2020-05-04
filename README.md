
## Receiver for WiFi security camera FTP event triggers 

Docker Container to receive movement images from a WiFi Security Camera over FTP and publish on MQTT

### Standalone Python script

To begin, assuming you have virtualenv installed:
```
virtualenv venv
source venv/bin/activate
pip install -r cam_receiver/requirements.txt
python cam_receiver/main.py
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

### Docker Compose

To build and run just the camera receiver container:
```
docker-compose build cam_receiver
docker-compose up cam_receiver
```


