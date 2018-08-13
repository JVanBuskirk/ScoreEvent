from pyo import *
from ScoreEvent import ScoreEvent

### Instrument
class Instr1:
    def __init__(self, duration, freq, amp):
        self.env = Fader(0.001, duration-0.005, duration, amp).play()
        self.osc = Sine(freq, mul=self.env).out()
        
s = Server().boot()

### Create the score
score = ScoreEvent(s, globals())

### Add events to the score ###
score.addEvent(['Instr1', 0, 0.5, midiToHz(60), 0.2])
score.addEvent(['Instr1', 0.5, 0.5, midiToHz(62), 0.2])
score.addEvent(['Instr1', 1, 0.5, midiToHz(64), 0.2])
score.addEvent(['Instr1', 1.5, 0.5, midiToHz(65), 0.2])
score.addEvent(['Instr1', 2, 0.5, midiToHz(67), 0.2])

### Play the score ###
score.play()

s.gui(locals())

