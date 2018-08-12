# chaos.py

# Chaotic Generators for PMask
# Copyright (C) 2000 by Hans Mikelson
# PMask by Maurizio Umberto Puxeddu

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

from math import pow, fabs, fmod, sin, cos, pi
from generator import *

class Lorenz(Generator):
    def __init__(self, val="x", h = 0.001, x = 19.1,  y = 9.8,  z = 48.0,
                 s = 10.0, r = 28.0, b = 2.6667):
        Generator.__init__(self)
        self.val = val
        self.h = h
	self.x = x
	self.y = y
	self.z = z
        self.s = s
	self.r = r
	self.b = b

    def valueAt(self, evaluationTime):
        h = evaluateAt(self.h, evaluationTime)
        s = evaluateAt(self.s, evaluationTime)
        r = evaluateAt(self.r, evaluationTime)
        b = evaluateAt(self.b, evaluationTime)

        x = self.x + h*(s*(self.y - self.x))
        y = self.y + h*(-self.x*self.z + r*self.x - self.y)
        self.z += h*(self.x*self.y - b*self.z)

        self.x = x
        self.y = y

        return eval('self.'+self.val)

if __name__ == '__main__':
    lx = Lorenz('x', 0.01)
    ly = Lorenz('y', 0.01)
    lz = Lorenz('z', 0.01)
    
    for i in range(2000):
        print lx.valueAt(i),  lx.valueAt(i), lz.valueAt(i)
