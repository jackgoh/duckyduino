# Ducky Duino
Arduino Based Rubber Ducky

## Supports
- Arduino Uno

## Pre-requisites
- dfu-programmer (brew install dfu-programmer)
- python3 (brew install python3)
- arduino-cli (https://github.com/arduino/arduino-cli)

## Installation
For OSX : `brew install dfu-programmer python3 arduino-cli`

Install arduino-cli (https://github.com/arduino/arduino-cli)

## Usage
This is the output of `--help`

    usage: duckyduino.py [-h] [--flash] [--unflash] [--upload]

    Rubber Ducky for Arduino Uno

    optional arguments:
    -h, --help      Show this help message and exit
    --flash, -f     Flash your Arduino into a malicious HID Device
    --unflash, -uf  Revert your Arduino into a regular serial device
    --upload, -up   Upload .ino sketch to Arduino

There are 2 steps to flash your Arduino into HID Keyboard as Rubber Ducky:
1. Upload duck sketch `python duckyduino.py -up sketch/helloworld`
2. Flash `python duckyduino.py -f`

To update duck scripts you have to restore your Arduino into default
`python duckyduino.py -uf`

## FAQ
How to put Arduino into DFU mode 

![](https://i.imgur.com/gVLYeHZ.jpg)




