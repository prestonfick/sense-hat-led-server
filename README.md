# Sense Hat LED Server

I made this LED server to let my family know my home-office status and whether it's OK to enter the office or not. This is a simple Flask server to handle Sense Hat LED control on a [Raspberry Pi 3](https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/) with a [Sense Hat](https://www.raspberrypi.org/products/sense-hat/). It has been tested runs on [Ubuntu 18.04 for Raspberry Pi](https://ubuntu.com/download/raspberry-pi) using Python 3. This is assumed to work in a home enviornment and is not secure.

# Installation Instructions

```
pip3 install flask
pip3 install Cython
apt-get install zlib1g-dev
apt-get install libjpeg-dev
pip3 install sense_hat

git clone https://github.com/RPi-Distro/RTIMULib.git
cd RTIMULib/Linux/python/
python3 setup.py build
python3 setup.py install
cd ../../..
```

# Run the Server in the Background

```
python3 sense-hat-led-server.py &
```

# Usage

Use the following HTTP requests to set the LED status:

```
http://<rpi-ip-address>:5000/ok-to-come-in
http://<rpi-ip-address>:5000/keep-out
http://<rpi-ip-address>:5000/off
```
