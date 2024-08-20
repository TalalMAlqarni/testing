#shoot(self) is the most importent
#testing
class SolenoidController:
    def __init__(self, solenoid_pin):
        self.solenoid_pin = solenoid_pin
        GPIO.setup(solenoid_pin, GPIO.OUT)
        GPIO.output(solenoid_pin, GPIO.LOW)

    def set_high(self):
        GPIO.output(self.solenoid_pin, GPIO.HIGH)

    def set_low(self):
        GPIO.output(self.solenoid_pin, GPIO.LOW)

    def shoot(self):
        GPIO.output(self.solenoid_pin, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(self.solenoid_pin, GPIO.LOW)    


def main():
    solenoid_controller = SolenoidController(24)

    # Set the solenoid high for 2 seconds
    solenoid_controller.set_high()
    time.sleep(2)

    # Set the solenoid low for 2 seconds
    solenoid_controller.set_low()
    time.sleep(2)


if __name__ == "__main__":
    main()
