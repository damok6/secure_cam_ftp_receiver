
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

Or if you want to run without a virtual environment:
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

To build camera receiver container and then run all containers in detatched mode:
```
docker-compose build cam_receiver
docker-compose up -d
```

If you get an error like:

```
mkdir: cannot create directory '/var/lib/grafana/plugins': Permission denied
```
this likely means the docker container created the directories as root and then was unable to write to the files in the directories. This can be fixed by running:

```
sudo chown -R 472:472 ./data_grafana/
```



this likely means the mqtt docker container created the directories as root and then was unable to write to the files in the directories. This can be fixed by running:


