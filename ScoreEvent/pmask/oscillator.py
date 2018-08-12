# oscillator.py

# PMask, a Python implementation of CMask
# Copyright (C) 2000 by Maurizio Umberto Puxeddu

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

#Added Gen to each class name to aviod conflict with pyo. Jeremy Van Buskirk 8/12/2018

from math import pow, fabs, fmod, sin, cos, pi
from generator import *

class SineGen(Generator):
    def __init__(self, T = 1.0, ph = 0.0):
        Generator.__init__(self)
        self.T = T
        self.ph = ph

    def valueAt(self, evaluationTime):
        t = evaluateAt(self.T, evaluationTime)
        ph = self.ph + evaluationTime / t
        return (1.0 + sin(2.0 * pi * ph)) / 2.0

class CosineGen(Generator):
    def __init__(self, T = 1.0, ph = 0.0):
        Generator.__init__(self)
        self.T = T
        self.ph = ph

    def valueAt(self, evaluationTime):
        t = evaluateAt(self.T, evaluationTime)
        ph = self.ph + evaluationTime / t
        return (1.0 + cos(2.0 * pi * ph)) / 2.0

class SawUpGen(Generator):
    def __init__(self, T = 1.0, ph = 0.0):
        Generator.__init__(self)
        self.T = T
        self.ph = ph

    def valueAt(self, evaluationTime):
        t = evaluateAt(self.T, evaluationTime)
        evaluationTime += t * self.ph
        evaluationTime = fmod(evaluationTime, t)
        if evaluationTime < 0:
            evaluationTime += t
        return evaluationTime / t

class SawDownGen(Generator):
    def __init__(self, T = 1.0, ph = 0.0):
        Generator.__init__(self)
        self.T = T
        self.ph = ph

    def valueAt(self, evaluationTime):
        t = evaluateAt(self.T, evaluationTime)
        evaluationTime += t * self.ph
        evaluationTime = fmod(evaluationTime, t)
        if evaluationTime < 0:
            evaluationTime += t
        return 1.0 - evaluationTime / t

class PowerUpGen(Generator):
    def __init__(self, T = 1.0, ph = 0.0, exponent = 0.0):
        Generator.__init__(self)
        self.T = T
        self.ph = ph
        self.exponent = pow(2.0, exponent)

    def valueAt(self, evaluationTime):
        t = evaluateAt(self.T, evaluationTime)
        evaluationTime += t * self.ph
        evaluationTime = fmod(evaluationTime, t)
        if evaluationTime < 0:
            evaluationTime += t

        return pow(evaluationTime / t, self.exponent)
        
class PowerDownGen(Generator):
    def __init__(self, T = 1.0, ph = 0.0, exponent = 0.0):
        Generator.__init__(self)
        self.T = T
        self.ph = ph
        self.exponent = pow(2.0, exponent)

    def valueAt(self, evaluationTime):
        t = evaluateAt(self.T, evaluationTime)
        evaluationTime += t * self.ph
        evaluationTime = fmod(evaluationTime, t)
        if evaluationTime < 0:
            evaluationTime += t
        return pow(1.0 - evaluationTime / t, self.exponent)

class SquareGen(Generator):
    def __init__(self, T = 1.0, ph = 0.0):
        Generator.__init__(self)
        self.T = T
        self.ph = ph

    def valueAt(self, evaluationTime):
        t = evaluateAt(self.T, evaluationTime)
        evaluationTime += t * self.ph
        evaluationTime = fmod(evaluationTime, t)
        if evaluationTime < 0:
            evaluationTime += t
        if evaluationTime < t/2:
            return 1.0
        else:
            return 0

class TriangleGen(Generator):
    def __init__(self, T = 1.0, ph = 0.0):
        Generator.__init__(self)
        self.T = T
        self.ph = ph

    def valueAt(self, evaluationTime):
        t = evaluateAt(self.T, evaluationTime)
        evaluationTime += t * self.ph
        t_2 = t / 2
        evaluationTime = fmod(evaluationTime, t)
        if evaluationTime < 0:
            evaluationTime += t
        if evaluationTime < t_2:
            return evaluationTime / t_2
        else:
            return 1.0 - (evaluationTime - t_2)/t_2

if __name__ == '__main__':
    f1 = SineGen(1.0)
    f2 = CosineGen(1.0)
    f3 = SawUpGen(1.0)
    f4 = SawDownGen(1.0)
    f5 = PowerUpGen(1.0, 0, 1.0)
    f6 = PowerUpGen(1.0, 0, 2.0)
    f7 = PowerUpGen(1.0, 0, -1.0)
    f8 = PowerDownGen(1.0, 0, 1.0)
    f9 = PowerDownGen(1.0, 0, 2.0)
    f10 = PowerDownGen(1.0, 0, -1.0)
    f11 = SquareGen(1.0)
    f12 = TriangleGen(1.0)
    f13 = SineGen(1.0, 0.3)
    f14 = CosineGen(1.0, 0.3)
    f15 = SawUpGen(1.0, 0.3)
    f16 = PowerUpGen(1.0, 0.3, 2.0)
    f17 = PowerDownGen(1.0, 0.3, 2.0)
    f18 = SquareGen(1.0, 0.3)
    f19 = TriangleGen(1.0, 0.3)
    
    t = -2.0
    step = 0.01
    for i in range(401):
        print t, f1.valueAt(t), f2.valueAt(t), f3.valueAt(t),\
              f4.valueAt(t), f5.valueAt(t), f6.valueAt(t),\
              f7.valueAt(t), f8.valueAt(t), f9.valueAt(t),\
              f10.valueAt(t), f11.valueAt(t), f12.valueAt(t),\
              f13.valueAt(t), f14.valueAt(t), f15.valueAt(t),\
              f16.valueAt(t), f17.valueAt(t), f18.valueAt(t), f19.valueAt(t)
        t += step
