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
    def __init__(self, server, globals=None): #EventParser arguments
        self.server = server #variable for the server
        self.globals = globals #global variables
        self._instruments = {} #empty dictionary for instruments

    def extractKwArgs(self, args): #arguements for extract key word function
        kwargs = "" #empty string.  used if there are no keyword args
        if "{" in args: # if their is a dictionary in the args
            p1 = args.find("{") #find the begining of the dictionary
            args, kwargs = args[:p1], args[p1:] #split the string at the beginning of the {
        if kwargs:
            kwargs = eval(kwargs) #evaluate any python code in the keyword dictionary
        return args, kwargs
                
    def addEvent(self, score):
        scoreParams = [] #empty list
        scoreParams.extend(score) #adds score to the list
        instr = scoreParams.pop(0) #removes the instrument name from the list and assigns it to the variable
        args = str(scoreParams).strip('[]') #it turns the rest into a string and removes the bracket
        args, kwargs = self.extractKwArgs(args) #runs the extract keyword function to split args and keyword args
        args = [x for x in scoreParams] #turns args back into a list.
        if instr not in self._instruments:
            self._instruments[instr] = [{"args": args, "kwargs": kwargs}] #if the instr is not in the dict. add it with it arguments
        else:
            self._instruments[instr].append({"args": args, "kwargs": kwargs}) #if the instr is in the dict. append a new instance
            
    def pmask(self, section):
        for note in section:
            self.addEvent(note)

    def play(self, time=0):
        self._playing = [] #empty list
        for instr in self._instruments: #for every instr (key) in the dict.
            for event in self._instruments[instr]: #for every event (value) assigned to each instr.  there can be multiple events for each instr.
                if event["args"][0] >= time:
                    self.server.setGlobalDel(event["args"][0]-time) #Sets the start time of the event on the server
                    self.server.setGlobalDur(event["args"][1]) #sets the duration of the event on the server
                    if not event["kwargs"]:
                        self._playing.append(self.globals[instr](*event["args"][1:])) #creates an instance of the instr. and puts it in the list * = variable number of arguments
                    else:
                        self._playing.append(self.globals[instr](*event["args"][1:], 
                                                                **event["kwargs"]))
        self.server.setGlobalDel(0) #returns server delay to 0
        self.server.setGlobalDur(0) #returns server durations to 0
