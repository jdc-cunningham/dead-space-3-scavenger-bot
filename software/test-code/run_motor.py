import RPi.GPIO as GPIO
import time

# Pin Definitions (BCM numbering)
# Use the GPIO number, not the physical pin number (e.g., GPIO 17 is physical pin 11)
AIN1 = 17
AIN2 = 18
# For Motor B:
# BIN3 = 22
# BIN4 = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)

# Configure PWM for speed control on one of the input pins
# You can use software PWM or hardware PWM pins for better performance
# For simplicity, we can use one PWM pin and one digital pin
# Here we will use PWM on AIN1 and digital on AIN2
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
pwm_motor_a = GPIO.PWM(AIN1, 100)  # 100 Hz frequency
pwm_motor_a.start(0) # Start with 0% duty cycle (stopped)

def drive_motor_a(speed, direction):
    # Speed is a value from 0 (stop) to 100 (full speed)
    if direction == "forward":
        GPIO.output(AIN2, GPIO.LOW)
        pwm_motor_a.ChangeDutyCycle(speed)
    elif direction == "reverse":
        GPIO.output(AIN2, GPIO.HIGH) # AIN2 controls reverse with AIN1 PWM
        # Note: Actual pin logic may vary by breakout board; adjust as needed
        # This setup assumes AIN1 (PWM) and AIN2 (LOW/HIGH) control speed/direction
        # A more common method is setting one high/low and the other PWM
        # A better approach (using two PWM pins):
        # if direction == "forward":
        #    pwm_a1.ChangeDutyCycle(speed)
        #    pwm_a2.ChangeDutyCycle(0)
        # elif direction == "reverse":
        #    pwm_a1.ChangeDutyCycle(0)
        #    pwm_a2.ChangeDutyCycle(speed)
        pass # The initial example is simpler

    # The most basic control (digital only for full speed):
    # if direction == "forward":
    #     GPIO.output(AIN1, GPIO.HIGH)
    #     GPIO.output(AIN2, GPIO.LOW)
    # elif direction == "reverse":
    #     GPIO.output(AIN1, GPIO.LOW)
    #     GPIO.output(AIN2, GPIO.HIGH)
    # elif direction == "stop":
    #     GPIO.output(AIN1, GPIO.LOW)
    #     GPIO.output(AIN2, GPIO.LOW)

try:
    print("Motor A Forward at 50% speed for 3 seconds")
    drive_motor_a(50, "forward") # This code needs refinement for speed, see comments above
    GPIO.output(AIN1, GPIO.HIGH) # For simple digital control
    GPIO.output(AIN2, GPIO.LOW)
    time.sleep(3)
    
    print("Stopping motor A")
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.LOW)
    time.sleep(2)

    print("Motor A Reverse at full speed for 3 seconds")
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.HIGH)
    time.sleep(3)

    print("Stopping motor A and cleaning up")
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.LOW)

except KeyboardInterrupt:
    pass

finally:
    pwm_motor_a.stop()
    GPIO.cleanup()