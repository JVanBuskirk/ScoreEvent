###Reworking of Olivier Belanger's original EventParser example
import random
from pyo import *
from ScoreEvent import ScoreEvent

### Orchestra ###
class Instr1:
    def __init__(self, duration, *args):
        self.f = Fader(0.001, duration-0.005, duration, args[1]).play()
        self.f.setExp(3)
        self.osc = SineLoop([args[0], args[0]*1.01], feedback=0.12, mul=self.f)
        self.filt = ButHP(self.osc, args[0]).out()



### Rendering ###
REALTIME = True

if REALTIME:
    s = Server().boot()
else:
    s = Server(buffersize=8, audio="offline").boot()
    s.recordOptions(dur=10, filename="rendered_score.wav")

lfo = Randi(-12.0, 12.0, 14)
notes = midiToHz([48.01,55.02,59.99,63.01,67,69.98,72.03,75.04])

### Create the score
score = ScoreEvent(s, globals())

starttime = 0
'''
### This will create events for 2 mins.
### Add an event to the score ###
while starttime < 120:
    dur = random.choice([.25, .75, 1])
    freq = random.choice(midiToHz([67,70,72,75,79,84,86,87,91])) + lfo
    amp = random.uniform(0.08, 0.15)
    score.addEvent(['Instr1', starttime, dur, freq, amp])
    starttime += random.choice([.125, .125, .25, .25])


### This will create 300 events
### Add an event to the score ###
for i in range(300):
    dur = random.choice([.25, .75, 1])
    freq = random.choice(midiToHz([67,70,72,75,79,84,86,87,91])) + lfo
    amp = random.uniform(0.08, 0.15)
    score.addEvent(['Instr1', starttime, dur, freq, amp])
    starttime += random.choice([.125, .125, .25, .25])
'''


### This will create events for 30 secs with a change of pitches at 15.
### Add an event to the score ###
while starttime < 30:
    dur = random.choice([.25, .75, 1])
    if starttime < 15:
        freq = random.choice(midiToHz([67,70,72,75,79,84,86,87,91])) + lfo
    else:
        freq = random.choice(midiToHz([64,67,69,72,76,81,83,84,88])) + lfo
    amp = random.uniform(0.08, 0.15)
    score.addEvent(['Instr1', starttime, dur, freq, amp])
    starttime += random.choice([.125, .125, .25, .25])




### Play the score ###
score.play()

if REALTIME:
    s.gui(locals())
else:
    s.start()