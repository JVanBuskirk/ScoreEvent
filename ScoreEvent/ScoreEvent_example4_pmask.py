import random
from pyo import *
from pmask import *
from ScoreEvent import ScoreEvent


###This a reworking on the principle PMask example

### Orchestra ###
class Instr1:
    def __init__(self, duration, *args):
        self.f = Fader(duration/2, duration/2, duration, args[1]).play()
        self.f.setExp(3)
        self.osc = SineLoop([args[0], args[0]*1.01], feedback=0.12, mul=self.f)
        self.filt = ButHP(self.osc, args[0]).mix(1)
        self.pan = Pan(self.filt, pan=args[2]).out()
        
class Instr2:
    def __init__(self, duration, *args):
        self.f = Fader(0.001, duration-0.005, duration, args[1]).play()
        self.f.setExp(3)
        self.osc = SineLoop([args[0], args[0]*1.01], feedback=0.12, mul=self.f)
        self.filt = ButHP(self.osc, args[0]).mix(1)
        self.pan = Pan(self.filt, pan=args[2]).out()

### Rendering ###
REALTIME = True

if REALTIME:
    s = Server().boot()
else:
    s = Server(buffersize=8, audio="offline").boot()
    s.recordOptions(dur=65, filename="rendered_score.wav")


### Create the score
score = ScoreEvent(s, globals())



#PMask

m = Mask(UniformRandom(), 100,
         LinearSegment([(0.0, 300.0), (10.0, 500.0), (20.0, 200)]))
frequency = Quantizer(m,
                      LinearSegment([(0.0, 10.0), (4.0, 80.0),  (20.0, 10.0)]),
                      LinearSegment([(0.0, 0.0), (4.0, 1.0), (20.0, 0.9)]),
                      0.0)

amplitude = Mask(SineGen(0.5),
                 LinearSegment([(0.0, 0.1), (20.0, 0)]),
                 LinearSegment([(0.0, 0.12), (5.0, 0.25), (20.0, 0)]))

density = Range(0.1, 0.5)
panning = Sine(0.1).range(0.1, 0.9) #you can use Pyo objects for Instr controls, but not pmask controls.

section = ScoreSection(0.0, 20.0, "Instr1", density, 10, frequency, amplitude, panning)

score.pmask(section.getScore())



# -----

frequency = List([1100, 1200, 1300, 2200, 2400, 2600])
amplitude = Mask(List([0.4, 0.2, 0.8, 1.0], 'swing'),
                 LinearSegment([(0.0, 0.02), (12.0, 0)]),
                 LinearSegment([(0.0, 0.03), (4.0, 0.05), (12.0, 0)]))

density = Range(0.1, 0.3)
panning = List([0.7, 0.3])
section =  ScoreSection(0.0, 12.0, "Instr2", density, 0.6, frequency, amplitude, panning)
section.translate(10.0)
score.pmask(section.getScore())

#delay even more and reverse it
section.translate(50.0)
section.reverse()
score.pmask(section.getScore())

# -----
frequency = List(tet12(0, 2, 4, 7))
amplitude = Mask(List([0.4, 0.2, 0.8, 1.0], 'swing'),
                 LinearSegment([(0.0, 0), (12.0, 0.03), (20.0, 0.0)]),
                 LinearSegment([(0.0, 0), (12.0, 0.05), (20.0, 0)]))

panning = Sine(0.1).range(0.1, 0.9)

section =  ScoreSection(0.0, 20.0, "Instr1", density, 10, frequency, amplitude, panning)
section.translate(30.0)
score.pmask(section.getScore())

# -----
frequency = Attractor(Mask(ExponentialRandom(), tet12(0), tet12(9)),
                      tet12(0, 2, 3, 7, 9),
                      LinearSegment([(0.0, 0.0), (5.0, 0.0), (12.0, 1.0)]),
                      1.0)
amplitude = Mask(List([0.4, 0.2, 0.8, 1.0], 'swing'),
                 LinearSegment([(0.0, 0), (12.0, 0.05), (25.0, 0.0)]),
                 LinearSegment([(0.0, 0), (12.0, 0.1), (25.0, 0)]))
density = Range(0.05, 0.1)
panning = List([0.7, 0.3])
section =  ScoreSection(0.0, 25.0, "Instr2", density, 0.6, frequency, amplitude, panning)
section.translate(20.0)
score.pmask(section.getScore())


### Play the score ###
score.play()
#score.play(time=30)

if REALTIME:
    s.gui(locals())
else:
    s.start()