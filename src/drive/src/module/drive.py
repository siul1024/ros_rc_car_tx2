import Adafruit_PCA9685
import Jetson.GPIO as GPIO
import threading, time


class Drive:
    # define
    channel_t = 0
    channel_s = 7
    throttle_stop = 290
    steering_center = 350
    throttle_bwd = 330
    throttle_fwd = 250
    steering_r = 420  # 420
    steering_l = 280  # 280
    pulse_freq = 50
    LED_PIN = 12

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(Drive.LED_PIN, GPIO.OUT)
        GPIO.output(Drive.LED_PIN, GPIO.LOW)
        self.pwm = Adafruit_PCA9685.PCA9685(address=0x40, busnum=1)
        self.pwm.set_pwm_freq(Drive.pulse_freq)
        self.throttle = Drive.throttle_stop
        self.steering = Drive.steering_center
        self.rec_status = False
        self.th = threading.Thread(target=self.led_blink)
        self.th.start()

    def car_brake(self):
        self.throttle = Drive.throttle_stop
        self.pwm.set_pwm(Drive.channel_s, 0, self.steering)
        self.pwm.set_pwm(Drive.channel_t, 0, self.throttle)

    def drive(self):
        self.pwm.set_pwm(Drive.channel_s, 0, self.steering)
        self.pwm.set_pwm(Drive.channel_t, 0, self.throttle)

    def led_blink(self):
        while self.rec_status:
            GPIO.output(Drive.LED_PIN, GPIO.HIGH)
            time.sleep(0.3)
            GPIO.output(Drive.LED_PIN, GPIO.LOW)
            time.sleep(0.3)
