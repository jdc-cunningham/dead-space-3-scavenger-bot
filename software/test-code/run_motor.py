import RPi.GPIO as GPIO
import time

# --- Pin Definitions ---
# Use BCM numbering
AIN1_PIN = 17  # Connect to IN1 for Motor A
AIN2_PIN = 27  # Connect to IN2 for Motor A
PWM_PIN = 18   # Connect to SLEEP/EN (A) for PWM Speed

# --- Setup ---
GPIO.setmode(GPIO.BCM)
GPIO.setup(AIN1_PIN, GPIO.OUT)
GPIO.setup(AIN2_PIN, GPIO.OUT)
GPIO.setup(PWM_PIN, GPIO.OUT)

# --- PWM Setup ---
# 100 Hz frequency (adjust as needed)
pwm = GPIO.PWM(PWM_PIN, 100)
pwm.start(0) # Start with 0% duty cycle (stopped)

def set_motor_speed(speed_percent):
    """Sets motor speed (0-100) using PWM duty cycle."""
    pwm.ChangeDutyCycle(speed_percent)
    print(f"Setting speed to {speed_percent}%")

def move_forward(speed_percent):
    """Moves motor forward at a given speed."""
    GPIO.output(AIN1_PIN, GPIO.HIGH)
    GPIO.output(AIN2_PIN, GPIO.LOW)
    set_motor_speed(speed_percent)
    print("Moving Forward")

def move_backward(speed_percent):
    """Moves motor backward at a given speed."""
    GPIO.output(AIN1_PIN, GPIO.LOW)
    GPIO.output(AIN2_PIN, GPIO.HIGH)
    set_motor_speed(speed_percent)
    print("Moving Backward")

def stop_motor():
    """Stops the motor."""
    GPIO.output(AIN1_PIN, GPIO.LOW)
    GPIO.output(AIN2_PIN, GPIO.LOW)
    set_motor_speed(0)
    print("Motor Stopped")

# --- Main Test ---
try:
    print("Testing DRV8833 Motor Control...")
    move_forward(50) # Move forward at 50% speed
    time.sleep(2)
    stop_motor()
    time.sleep(1)
    move_backward(75) # Move backward at 75% speed
    time.sleep(2)
    stop_motor()
    time.sleep(1)

except KeyboardInterrupt:
    print("Program interrupted by user.")

finally:
    pwm.stop()
    GPIO.cleanup() # Clean up GPIO settings