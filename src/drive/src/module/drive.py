import Adafruit_PCA9685


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

    def __init__(self):
        self.pwm = Adafruit_PCA9685.PCA9685(address=0x40, busnum=1)
        self.pwm.set_pwm_freq(Drive.pulse_freq)
        self.throttle = Drive.throttle_stop
        self.steering = Drive.steering_center
        self.mode = True

    def car_brake(self):
        self.throttle = Drive.throttle_stop
        self.pwm.set_pwm(Drive.channel_s, 0, self.steering)
        self.pwm.set_pwm(Drive.channel_t, 0, self.throttle)

    def drive(self):
        self.pwm.set_pwm(Drive.channel_s, 0, self.steering)
        self.pwm.set_pwm(Drive.channel_t, 0, self.throttle)

