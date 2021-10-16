import RPi.GPIO as GPIO
import time
import smtplib, ssl
# setup GPI0
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 100)
pwm.start(0)
duty1 = float(90) / 10.0 + 2.5
pwm.ChangeDutyCycle(duty1)
time.sleep(0.5)
duty1 = float(180) / 10.0 + 2.5
pwm.ChangeDutyCycle(duty1)
time.sleep(0.5)
GPIO.cleanup(18)