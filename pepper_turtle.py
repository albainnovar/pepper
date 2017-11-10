# encoding: utf-8
from __future__ import division
from naoqi import ALProxy
from pepper_data import IP, PORT
from math import radians


class Turtle:
    def __init__(self, ip=IP, port=PORT, ask_ok=True):
        self.tts = ALProxy("ALTextToSpeech", ip, port)
        self.motion = ALProxy("ALMotion", ip, port)
        self.ip = ip
        self.port = port
        self.tts.say("You can control me now.")
        self.ask_ok = ask_ok

    def _movement(self, template, measure, x=0, y=0, degree=0):
        self.tts.say(template.format(measure))
        can_move = self.motion.moveTo(x/100, y/100, radians(degree))
        if not can_move:
            self.say('There is an obstacle. I can not move.')


    def forward(self, distance):
        "Go `distance` in centimeters."
        if self.out_of_interval(0, 200, distance):
            return
        self._movement("I go forward {} centimeters.", distance, x=distance)

    def backward(self, distance):
        "Go `distance` in centimeters."
        if self.out_of_interval(0, 200, distance):
            return
        self._movement("I go backward {} centimeters.", distance, x=-distance)

    def left(self, degree):
        "Turn right `degree` degrees."
        if self.out_of_interval(0, 180, degrees):
            return
        self._movement("I turn left {} degrees.", degree, degree=degree)

    def right(self, degree):
        "Turn right `degree` degrees."
        if self.out_of_interval(0, 180, degree):
            return
        self._movement("I turn right {} degrees.", degree, degree=-degree)

    def move_left(self, distance):
        "Go `distance` in centimeters."
        if self.out_of_interval(0, 40, distance):
            return
        self._movement("I go left {} centimeters.", distance, y=distance)

    def move_right(self, distance):
        "Go `distance` in centimeters."
        if self.out_of_interval(0, 40, distance):
            return
        self._movement("I go right {} centimeters.", distance, y=-distance)

    def say(self, text):
        self.tts.say(text)

    def out_of_interval(self, min, max, value):
        if value > max or value < min:
            self.say("This value should be between {} and {}.".format(min, max))
