#!/usr/bin/python
import argparse
import subprocess
import commands

HID_HEX = "./flash-bin/Arduino-keyboard.hex"
SERIAL_HEX = "./flash-bin/Arduino-usbserial.hex"

def main():

    # Instantiate ArgumentParser
    parser = argparse.ArgumentParser(description='Arduino Based Rubby Ducky')
    parser.add_argument('--flash', '-f', action="store_true", 
        help='Flash your Arduino Uno into a malicious HID Device')
    parser.add_argument('--unflash', '-uf', action="store_true", 
        help='Revert your Arduino Uno into a regular serial device')
    parser.add_argument('--upload', '-up', metavar='[sketch_name]', help='Upload sketch to arduino')

    # Parse arguments
    args = parser.parse_args()

    # Ensure dfu-programmer exists as a command
    status, _ = commands.getstatusoutput('dfu-programmer --help')
    if status != 0:
        print("Unable to call dfu-programmer command. Is it installed or in PATH?")
        exit(1)

    # Flash as HID
    if args.flash:
        print "Please put your Arduino into DFU mode. Press Enter to continue when complete."
        raw_input()
        subprocess.call(["dfu-programmer", "atmega16u2", "erase"])
        subprocess.call(["dfu-programmer", "atmega16u2", "flash", "--debug", "1", HID_HEX])
        subprocess.call(["dfu-programmer", "atmega16u2", "reset"])
        print "Done! You may now use your new Rubber Ducky !\n"

    # Flash as a regular serial device
    elif args.unflash:
        print "Please put your Arduino into DFU mode. Press Enter to continue when complete."
        raw_input()
        subprocess.call(["dfu-programmer", "atmega16u2", "erase"])
        subprocess.call(["dfu-programmer", "atmega16u2", "flash", "--debug", "1", SERIAL_HEX])
        subprocess.call(["dfu-programmer", "atmega16u2", "reset"])
        print "Done! You may now use your Arduino as a regular serial device!\n"

    elif args.upload:
        subprocess.call(["arduino-cli", "compile", "--fqbn", "arduino:avr:uno", "sketch/" + str(args.upload)])
        subprocess.call(["arduino-cli", "upload", "-p", "/dev/cu.usbmodem14101", "--fqbn", "arduino:avr:uno", "sketch/helloworld"])
        # print "Done! You may now flash your Arduino!\n"

    # Print default help if none provided
    else:
        print parser.print_help()

if __name__ == "__main__":
    main()
