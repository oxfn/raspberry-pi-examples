#!/usr/bin/python
import sys
import RPi.GPIO as GPIO
from time import sleep

""" Basic GPIO port output example. This programs simply blinks on LED by specified interval

    Usage:
    blink.py [port] [interval]
"""

def main(args):
    """Main procedure"""

    # Check port argument
    port = int(args[0]) if len(args) > 0 else 11

    # Check interval argument
    interval = float(args[1]) if len(args) > 1 else 0.3

    # Go blinking
    blink(port, interval)

def blink(port, interval):
    """Blink procedure"""

    # Disable GPIO warnings about busy ports etc
    GPIO.setwarnings(False)

    # Debug info
    print("PI REVISION:", GPIO.RPI_REVISION)
    print("PROGRAM: BLINK")
    print("PORT:", port)
    print("INTERVAL:", interval)

    # Set pin numbering mode
    GPIO.setmode(GPIO.BOARD)

    # Begin port output
    GPIO.setup(port, GPIO.OUT)

    # Eternal loop
    while True:

        # Set ~port to 0
        GPIO.output(port, GPIO.LOW)

        # Wait
        sleep(interval)

        # Set port to 1
        GPIO.output(port, GPIO.HIGH)

        # Wait
        sleep(interval)

# Entry point
if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt as e:
        print("BREAK")
    except Exception as e:
        print("ERROR:", e)

    GPIO.cleanup()
    
        
