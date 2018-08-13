# score.py

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

#import UserList, types
from exception import *
from generator import *

#Updated by Jeremy Van Buskirk 8/6-8/12 2018

class ScoreSection:
    def __init__(self, begin, end, number, time, duration, *args):
        self.begin = begin
        self.end = end
        self.number = number
        self.time = time
        self.duration = duration
        self.args = args
        self.apply_list = []
        self.score_list = []
        self.processEvent()
        
    def processEvent(self):
        t = self.begin
        while t < self.end:
            self.apply_list = [self.number, t, evaluateAt(self.duration, t)]
            for pfield in self.args:
                self.apply_list.append(evaluateAt(pfield, t))
            #print(self.apply_list)
            t += evaluateAt(self.time, t)
            self.score_list.append(self.apply_list)
        #print(self.score_list)
            
    def translate(self, time, mode = 'absolute'):
        if mode == 'absolute':
            tmin = None
            for event in self.score_list:
                if tmin == None or event[1] < tmin:
                    tmin = event[1]
            offset = time - tmin
        else:
            offset = time

        for i in self.score_list:
            i[1] += offset
            
    def reverse(self):
        tmin = None
        tmax = None
        for event in self.score_list:
            if tmin == None or event[1] < tmin:
                tmin = event[1]
            if tmax == None or event[1] > tmax:
                tmax = event[1]

        for event in self.score_list:
            event[1] = tmax - (event[1] - tmin)

        self.score_list.reverse()
        
    def getScore(self):
        return self.score_list
        
            
