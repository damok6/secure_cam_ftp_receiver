from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer
import base64
import paho.mqtt.publish as publish

#TODO: Make dynamic
mqtt_host = '192.168.1.55'
mqtt_port = 1883

class MyHandler(FTPHandler):

    def on_connect(self):
        print("%s:%s connected" % (self.remote_ip, self.remote_port))

    def on_disconnect(self):
        # do something when client disconnects
        pass

    def on_login(self, username):
        # do something when user login
        pass

    def on_logout(self, username):
        # do something when user logs out
        pass

    def on_file_sent(self, file):
        # do something when a file has been sent
        pass

    def on_file_received(self, file):
        # do something when a file has been received
        print('on_file_received', file)
        encoded_image = self.convertImageToBase64(file)
        print('encoded image ends with:',encoded_image[-10:-1])
        publish.single(
            topic='todo/replace/topic/name',
            payload=encoded_image,
            hostname=mqtt_host,
            port=mqtt_port
        )

    def on_incomplete_file_sent(self, file):
        # do something when a file is partially sent
        pass

    def on_incomplete_file_received(self, file):
        # remove partially uploaded files
        import os
        os.remove(file)

    def convertImageToBase64(self, path):
        with open(path, "rb") as image_file:
            encoded = base64.b64encode(image_file.read())
            return encoded


def main():
    authorizer = DummyAuthorizer()
    authorizer.add_user('user', '12345', homedir='.', perm='elradfmwMT')
    authorizer.add_anonymous(homedir='.', perm='elradfmwMT')

    handler = MyHandler
    handler.authorizer = authorizer
    server = FTPServer(('', 21000), handler)
    server.serve_forever()

if __name__ == "__main__":
    main()
