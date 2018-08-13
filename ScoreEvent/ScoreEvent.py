"""
ScoreEvent is a reworking of EventParser by Jeremy Van Buskirk

Score format:

score.addEvent(starttime, duration, *args, **kwargs)

Class_name {class reference}: The name of the class which should play the event,
starttime {float}: Start time of the event, in seconds. 
duration {float}: Start time of the event, in seconds.
*args {list of floats or pyoObjects}: user-defined arguments (optional).
**kwargs {dictionary}: user-defined keyword arguments (optional).

# Notes:
#This is my hack of the EventParser class. 
#The format was inspired by SuperCollider's Ctk object.

"""

"""
Copyright 2017-2018 Olivier Belanger, Jeremy Van Buskirk

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with pyo.  If not, see <http://www.gnu.org/licenses/>.
"""


class ScoreEvent:
    def __init__(self, server, globals=None):
        self.server = server
        self.globals = globals
        self._instruments = {}

    def extractKwArgs(self, args):
        kwargs = ""
        if "{" in args:
            p1 = args.find("{")
            args, kwargs = args[:p1], args[p1:]
        if kwargs:
            kwargs = eval(kwargs)
        return args, kwargs
                
    def addEvent(self, score):
        scoreParams = []
        scoreParams.extend(score)
        instr = scoreParams.pop(0)
        args = str(scoreParams).strip('[]')
        args, kwargs = self.extractKwArgs(args)
        args = [x for x in scoreParams]
        if instr not in self._instruments:
            self._instruments[instr] = [{"args": args, "kwargs": kwargs}]
        else:
            self._instruments[instr].append({"args": args, "kwargs": kwargs})
            
    def pmask(self, section):
        for note in section:
            self.addEvent(note)

    def play(self, time=0):
        self._playing = []
        for instr in self._instruments:
            for event in self._instruments[instr]:
                if event["args"][0] >= time:
                    self.server.setGlobalDel(event["args"][0]-time)
                    self.server.setGlobalDur(event["args"][1])
                    if not event["kwargs"]:
                        self._playing.append(self.globals[instr](*event["args"][1:]))
                    else:
                        self._playing.append(self.globals[instr](*event["args"][1:], 
                                                                **event["kwargs"]))
        self.server.setGlobalDel(0)
        self.server.setGlobalDur(0)
