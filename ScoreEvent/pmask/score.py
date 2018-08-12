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

"""
class ScoreEvent:
    def __init__(self, kind, *args):
        self.kind = kind
        self.pfields = []
        self.pfields.extend(args)

    def __str__(self):
        string = self.kind
        for pfield in self.pfields:
            if type(pfield) is types.StringType:
                string += '"' + pfield + '"'
            else:
                string += ', ' + str(pfield)
        notes = "score.addEvent([" + string + "])" #change JVB 8/6/2018
        return notes

class IStatement(ScoreEvent):
    def __init__(self, number, time, duration, *args):
        apply_list = [self, '', number, time, duration] #change JVB 8/6/2018 - Why do I need the blank string
        apply_list.extend(args)
        apply(ScoreEvent.__init__, apply_list)

class FStatement(ScoreEvent):
    def __init__(self, number, time, length, type, *args):
        apply_list = [self, 'f', number, time, length, type]
        apply_list.extend(args)
        apply(ScoreEvent.__init__, apply_list)

class ScoreSection(UserList.UserList):
    def __init__(self, begin, end,
                 number, time, duration, *args):
        UserList.UserList.__init__(self)

        t = begin
        while t < end:
            apply_list = [number, t, evaluateAt(duration, t)]
            for pfield in args:
                apply_list.append(evaluateAt(pfield, t))
            istatement = apply(IStatement, apply_list)
            print(istatement)
            self.add(istatement)
            t += evaluateAt(time, t)

    def add(self, istatement):
        if not isinstance(istatement, IStatement):
            raise BadArgument
        self.append(istatement)

    def translate(self, time, mode = 'absolute'):
        if mode == 'absolute':
            tmin = None
            for event in self.data:
                if tmin == None or event.pfields[1] < tmin:
                    tmin = event.pfields[1]
            offset = time - tmin
        else:
            offset = time

        for i in self.data:
            i.pfields[1] += offset

    def reverse(self):
        tmin = None
        tmax = None
        for event in self.data:
            if tmin == None or event.pfields[1] < tmin:
                tmin = event.pfields[1]
            if tmax == None or event.pfields[1] > tmax:
                tmax = event.pfields[1]

        for event in self.data:
            event.pfields[1] = tmax - (event.pfields[1] - tmin)

        self.data.reverse()

    def __str__(self):
        if len(self.data):
            s = str(self.data[0])
            for i in self.data[1:]:
                s += '\n' + str(i)
            return s
        return ''
"""
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
        
            
