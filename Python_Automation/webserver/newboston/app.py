import RPi.GPIO as GPIO
from flask import Flask, render_template, request

pin=21
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.OUT)
app =Flask(__name__)

@app.route("/bitches")
def bitches():
	return "<h2>heyoo<h2><br><h1>whats up bitches<h1>"

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/shibby")
def shibby():
	return 'this is a shibby test'


@app.route("/profile/<name>")
def profile(name):
	if name=='on':
		GPIO.output(pin,1)
	else:
		GPIO.output(pin,0)
	return name




if __name__ =="__main__":
	print 'main is now '
	app.run(host='0.0.0.0', port=80, debug=True)
	for i in range (0,5):
		print "heyoo"
   
