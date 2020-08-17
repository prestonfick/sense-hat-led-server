from flask import Flask
from sense_hat import SenseHat

app = Flask(__name__)

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

def scene_keep_out():
    R = red
    scene = [
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    ]
    return scene

def scene_ok_to_come_in():
    G = green
    scene = [
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G,
    ]
    return scene

def scene_off():
    N = nothing
    scene = [
    N, N, N, N, N, N, N, N,
    N, N, N, N, N, N, N, N,
    N, N, N, N, N, N, N, N,
    N, N, N, N, N, N, N, N,
    N, N, N, N, N, N, N, N,
    N, N, N, N, N, N, N, N,
    N, N, N, N, N, N, N, N,
    N, N, N, N, N, N, N, N,
    ]
    return scene

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/keep-out')
def keep_out():
    s.set_pixels(scene_keep_out())
    return 'Keep Out Set'

@app.route('/ok-to-come-in')
def ok_to_come_in():
    s.set_pixels(scene_ok_to_come_in())
    return 'OK To Come In Set'

@app.route('/off')
def off():
    s.set_pixels(scene_off())
    return 'Off'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
