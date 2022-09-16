from flask import Flask
from threading import Thread
import store_service

rest_port = 5001
app = Flask(__name__)

if __name__ == '__main__':
    t = Thread(target=store_service.start_service)
    t.start()
    app.run(host='0.0.0.0', port=rest_port)

'''@app.before_first_request
def launch_consumer():
    print("Hilo ejecutandose")
    t = Thread(target=store_service.start_service())
    t.start()'''
