"""
EventParser - Jeremy Van Buskirk hack!!

Score format:

score.addEvent(starttime, duration, *args, **kwargs)

Class_name {class reference}: The name of the class which should play the event,
starttime {float}: Start time of the event, in seconds. 
duration {float}: Start time of the event, in seconds.
*args {list of floats or pyoObjects}: user-defined arguments (optional).
**kwargs {dictionary}: user-defined keyword arguments (optional).
 
"""
# Notes:
#This is my hack of the EventParser class. It format was inspired by
#SuperCollider's Ctk object.
#This allows you to add pyo objects as arguments to the synths


class EventParser:
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
        testScore = []
        testScore.extend(score)
        instr = testScore.pop(0)
        args = str(testScore).strip('[]')
        args, kwargs = self.extractKwArgs(args)
        args = [x for x in testScore]
        if instr not in self._instruments:
            self._instruments[instr] = [{"args": args, "kwargs": kwargs}]
        else:
            self._instruments[instr].append({"args": args, "kwargs": kwargs})

    def play(self):
        self._playing = []
        for instr in self._instruments:
            for event in self._instruments[instr]:
                self.server.setGlobalDel(event["args"][0])
                self.server.setGlobalDur(event["args"][1] + 0.2)
                if not event["kwargs"]:
                    self._playing.append(self.globals[instr](*event["args"][1:]))
                else:
                    self._playing.append(self.globals[instr](*event["args"][1:], 
                                                             **event["kwargs"]))
        self.server.setGlobalDel(0)
        self.server.setGlobalDur(0)
