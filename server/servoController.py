import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(03, GPIO.OUT)
pwm=GPIO.PWM(03, 50)

def start():
  pwm.start(0)

def setAngle(angle):
  duty = angle / 18 + 2
  GPIO.output(03, True)
  pwm.ChangeDutyCycle(duty)
  sleep(1)
  GPIO.output(03, False)
  pwm.ChangeDutyCycle(0)

def end():
  pwm.stop()
  GPIO.cleanup()
