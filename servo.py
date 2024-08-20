# use this three only:
# servo_controller = ServoController(18, 15)
# servo_controller.catch()
# servo_controller.release()
############################
# importent:
# from gpiozero import AngularServo
# from time import sleep
# import RPi.GPIO as GPIO
#cccc
class ServoController:
    def __init__(self, servo1_pin, servo2_pin):
        self.servo1 = AngularServo(servo1_pin, min_angle=0, max_angle=180,
                                   min_pulse_width=0.0005,
                                   max_pulse_width=0.0025)
        self.servo2 = AngularServo(servo2_pin, min_angle=0, max_angle=180,
                                   min_pulse_width=0.0005,
                                   max_pulse_width=0.0025)

    def catch(self):
        self.servo1.angle = 0
        self.servo2.angle = 180
        time.sleep(2)

    def release(self):
        self.servo1.angle = 90
        self.servo2.angle = 90
        time.sleep(2)

# we may test this
# whil (self.servo1.angle != 0)
# self.servo1.angle = self.servo1.angle + 10
# i dont know it can be faster

def main():
    servo_controller = ServoController(18, 15)

    while True:
        x = input()

        if x == "1":
            servo_controller.catch()
        elif x == "2":
            servo_controller.release()


if __name__ == "__main__":
    main()
