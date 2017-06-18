import RPi.GPIO as GPIO
from flask import Flask, render_template, request
from flask_socketio import SocketIO:

app =Flask(__name__)
pin=21
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.OUT)


@app.route("/")
def index():
	return render_template('index.html')

#Turns on output if "on" is entered in name parameter otherwise turns off
@app.route("/profile/<name>")
def profile(name):
	if name=='on':
		GPIO.output(pin,1)
	else:
		GPIO.output(pin,0)
	return name


if __name__ =="__main__":
	socket.run(host='0.0.0.0', port=80, debug=True)
   
