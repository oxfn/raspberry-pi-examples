#!/usr/bin/python
import sys
import RPi.GPIO as GPIO
from time import sleep

""" This example demonstrates basic reading from port. Program simply runs
    in loop, reads value from control port (with button) and sends its state
    to output port (with LED)

    Usage: led_button.py [port]
"""

def main(args):
    """Main program"""

    # Get parameters from command line
    led_port = int(args[0]) if len(args) > 0 else 11
    button_port = int(args[1]) if len(args) > 1 else 12

    # Debug info
    print("PI REVISION:", GPIO.RPI_REVISION)
    print("PROGRAM: LED_BUTTON")
    print("LED PORT:", led_port)
    print("BUTTON PORT:", button_port)

    # Disable GPIO warnings about busy ports etc
    GPIO.setwarnings(False)

    # Set pin numbering mode
    GPIO.setmode(GPIO.BOARD)

    # Write to LED port
    GPIO.setup(led_port, GPIO.OUT, initial=GPIO.HIGH)

    # Read from port
    GPIO.setup(button_port, GPIO.IN)

    # Remember previous value
    pval = GPIO.HIGH

    # Run in cycle
    while True:

        # Read from button port
        val = GPIO.input(button_port)

        # Do things only if value has changed
        if val != pval:

            # Show human readable state info
            if val == GPIO.HIGH:
                print("OFF")
            elif val == GPIO.LOW:
                print("ON")

            # Send value to LED port
            GPIO.output(led_port, val)

            # Remember changed value
            pval = val

        # Cool hack to not load CPU for 100%
        sleep(0.1)

# Entry point
if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt as e:
        print("BREAK")
    except Exception as e:
        print("ERROR:", e)

    # Let's be gentle
    GPIO.cleanup()
