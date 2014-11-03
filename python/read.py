#!/usr/bin/python
import sys
import RPi.GPIO as GPIO
from time import sleep

""" Basic GPIO port input example. This programs reads data from digital GPIO port

    Usage:
    led_blink.py [port] [interval]
"""

DEFAULT_PORT = 12
DEFAULT_INTERVAL = 0.2

def main(args):
    """Main procedure"""

    # Check port argument
    port = int(args[0]) if len(args) > 0 else DEFAULT_PORT

    # Check interval argument
    interval = float(args[1]) if len(args) > 1 else DEFAULT_INTERVAL

    # Go blinking
    blink(port, interval)

def blink(port, interval):
    """Blink procedure"""

    # Disable GPIO warnings about busy ports etc
    GPIO.setwarnings(False)

    # Debug info
    print("PI REVISION:", GPIO.RPI_REVISION)
    print("PROGRAM: PORT_READ")
    print("PORT:", port)

    # Set pin numbering mode
    GPIO.setmode(GPIO.BOARD)

    # Begin port output
    GPIO.setup(port, GPIO.IN)
    
    # Start value
    val = -1

    # Eternal loop
    while True:

        # Wait
        sleep(interval)

        # Read next value from port
        new_val = GPIO.input(port)

        # Only if value has changed
        if new_val != val:

            # Save it and trace it
            val = new_val
            if val == GPIO.LOW:
                print('OFF')
            else:
                print('ON')

# Entry point
if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt as e:
        print("BREAK")
    except Exception as e:
        print("ERROR:", e)

    GPIO.cleanup()
    
        
