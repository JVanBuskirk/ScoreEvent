# ScoreEvent
ScoreEvent is a score processor and player class for Pyo.  ScoreEvent incorporates a modified version of PMask for alogrithmic composition.

### Basic Example

```python
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

```

### Basic PMask Example
```python
from pyo import *
from pmask import *
from ScoreEvent import ScoreEvent

### Instrument
class Instr1:
    def __init__(self, duration, freq, amp):
        self.env = Fader(0.001, duration-0.005, duration, amp).play()
        self.osc = Sine(freq, mul=self.env).out()
        
s = Server().boot()

### Create the score
score = ScoreEvent(s, globals())

### PMask
frequency = Mask(UniformRandom(), 220, 880)
amp = Range(0.1, 0.4)
density = Range(0.1, 0.3)
duration = 0.5
section = ScoreSection(0, 10, "Instr1", density, duration, frequency, amp)

### Add events to the score ###
score.pmask(section.getScore())

### Play the score ###
score.play()

s.gui(locals())
```

Pyo is written by Olivier Bélanger

PMask was written by Maurizio Umberto Puxeddu.  It is a python implementation of CMask by Andre Bartetzki. 

more information:
### Pyo
http://ajaxsoundstudio.com/software/pyo/

### PMask
https://sourceforge.net/projects/pythonsound/

### CMask
https://www.bartetzki.de/en/software.html
