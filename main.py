# from adafruit_ads1x15.analog_in import AnalogIn
# import adafruit_ads1x15.ads1115 as ADS
# import board
# import busio
# from time import sleep
# i2c = busio.I2C(board.SCL, board.SDA)
# ads = ADS.ADS1115(i2c)
# chan = AnalogIn(ads, ADS.P0)
# while True:
#     prec = chan.voltage
#     print("Value: ", round(prec, 2))
#     # print("Value:",chan.voltage)
#     #print(((chan.value /1024) * 10) )

#     sleep(1)
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/moisture")
def moist():
    return render_template('index.html')


@app.route("/temprature")
def temp():
    return render_template('index.html')
