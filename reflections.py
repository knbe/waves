from manim import *
from math import exp, sqrt, pi, ceil, floor
from vec3 import *
import numpy as np

class ResonanceTube(Scene):
    def construct(s):
        numberplane = NumberPlane() 

        f = .340
        v = .340
        wavelength = v / f
        A = .1
        omega = 2 * pi * f
        L = 2.0
        k = 2 * pi / wavelength

        pointSpacingTarget = .05
        numSamplingPoints = ceil(L / pointSpacingTarget)
        pointSpacing = L / (numSamplingPoints - 1)
        points = [0 for i in range(numSamplingPoints)]

        dispLine = Line()

        print(points)

        s.add(numberplane)
        s.wait(1)

        t0 = 0
        dt = .01

