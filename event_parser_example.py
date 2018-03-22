import random
from pyo import *
from EventParser import EventParser

### Orchestra ###
class Instr1:
    def __init__(self, duration, *args):
        self.f = Fader(0.001, duration-0.005, duration, args[1]).play()
        self.f.setExp(3)
        self.osc = SineLoop([args[0], args[0]*1.01], feedback=0.12, mul=self.f)
        self.filt = ButHP(self.osc, args[0]).out()

class Rhythm:
    def __init__(self, duration, *args):
        self.env = CosTable([(0,0), (32,1), (1000,.25), (8191,0)])
        rhythms = [[2,2,1,1,1,1,4], [1,2,1,2,2,1,2,1,2,1,1],[4,2,1,1,2,2,1.3,1.3,1.4]]
        self.seq = Seq(.125, random.choice(rhythms), poly=1, onlyonce=True).play()
        self.amp = TrigEnv(self.seq, self.env, .125, mul=args[1])
        self.osc = Lorenz([args[0], args[0]*1.01], args[2], True, mul=self.amp)
        self.disto = Disto(self.osc, drive=0.9, slope=0.9, mul=0.4)
        self.bp = ButBP(self.disto, freq=1000, q=0.7).out()

class Chord:
    def __init__(self, duration, *args, **kwargs):
        self.f = Fader(1, 1, duration, args[0]).play()
        self.o1 = LFO(kwargs["f1"], sharp=0.95, type=2, mul=self.f).out()
        self.o2 = LFO(kwargs["f2"], sharp=0.95, type=2, mul=self.f).out(1)
        self.o3 = LFO(kwargs["f3"], sharp=0.95, type=2, mul=self.f).out()
        self.o4 = LFO(kwargs["f4"], sharp=0.95, type=2, mul=self.f).out(1)



### Rendering ###
REALTIME = False

if REALTIME:
    s = Server().boot()
else:
    s = Server(buffersize=8, audio="offline").boot()
    s.recordOptions(dur=9, filename="rendered_score.wav")

lfo = Sine(1).range(440, 550)
lfo2 = Randi(300, 800, 3)
notes = midiToHz([48.01,55.02,59.99,63.01,67,69.98,72.03,75.04])
cdict = {"f1": random.choice(notes), "f2": random.choice(notes),
             "f3": random.choice(notes), "f4": random.choice(notes)}

### Create the score
score = EventParser(s, globals())

### Add an event to the score ###
score.addEvent(['Instr1', 0, 6, lfo, 0.2])
score.addEvent(['Instr1', 0, 8, lfo2, 0.2])
score.addEvent(['Rhythm', 3, 3, 0.25, 1, 0.5])
score.addEvent(['Chord', 0, 6, 0.03, cdict])

### Play the score ###
score.play()

if REALTIME:
    s.gui(locals())
else:
    s.start()