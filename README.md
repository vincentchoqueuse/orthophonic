# 🎵 Orthophonic

**Orthophonic** is a research-based Python library for algorithmic music composition, leveraging mathematical principles such as **zero-crossings of oscillators, non-uniform sampling, and structured event distributions**. By bridging signal processing and musical structures, Orthophonic provides a framework for generating rhythms, pitch scales, and musical sequences based on rigorous mathematical foundations.

## 🚀 Features

- **Mathematically-driven composition**: Generates musical structures using **oscillator zero-crossings** and **event spacing optimization**.
- **Harmonic & Rhythmic Generation**: Supports **equal temperament**, **custom scales**, and **rhythmic patterns**.
- **Grid-Based Event Placement**: Uses a **master grid** for time and frequency structuring.
- **Customizable Phase & Frequency Modulation**: Enables fine control over rhythm and pitch via local oscillators.
- **Seamless Integration**: Works with **Ableton Live

## 📦 Installation

> Work with python 3.12

To install Orthophonic, simply run:


```bash
pip install -r requirements.txt
```

```bash
pip install -e .
```

Here’s an improved version of your **README** section with better clarity, structure, and formatting:

---

### 🎵 **Note for Ableton Users**  

You can send information directly to **Ableton Live** using **PyLive**:  
🔗 [PyLive GitHub Repository](https://github.com/ideoforms/pylive)  

To enable this functionality, you need to install **Remote Scripts** in Ableton’s folder and configure **Ableton Live** accordingly.  

📌 **Installation Guide:**  

Follow the setup instructions here:  
🔗 [AbletonOSC Installation Guide](https://github.com/ideoforms/AbletonOSC?tab=readme-ov-file#installation)  

## Getting Started

### Run some examples

You can find several examples in the examples folder

```
cd examples
```

Then simply run :

```
python drums_example.py # create a drum track in the first clip of the first track in Ableton Live
python drums_example_midi.py # export a drum track to a midi file
```


### Example


```
from orthophonic.base import Vector, Sine_Zeros
from orthophonic.utils import generate_grid, create_clip
from orthophonic.sequence import Sequence
import numpy as np
import live

# intial parameters
track_index = 0
clip_index = 0
track_index = 0
sigma_time = 0.4
repeat = 4

# generate master grid
grid = generate_grid(N=16, repeat=repeat)

# custom euclidean rhythms
v1 = Sine_Zeros(3, 16, repeat=repeat)               # kick pattern
v2 = Sine_Zeros(2, 16, repeat=repeat).add(4)        # snare pattern
v3 = Sine_Zeros(5 , 16, repeat=repeat).add(3)
v4 = Sine_Zeros(7, 16, repeat=repeat).add(1)
v5 = Sine_Zeros(9, 16, repeat=repeat).add(2)
v6 = Sine_Zeros(5, 16, repeat=repeat).add(1)
v_list = [v1, v2, v3, v4, v5, v6]

# generate list of pitch. Each pitch correspond to a note of a the drumkit
pitch_list = np.array([36, 41, 44, 57, 49, 55]) + 0

# connect to Ableton / create clip
set = live.Set(scan=True)
clip = create_clip(set, track_index, clip_index, 16, erase=True)

for index, v in enumerate(v_list):
    N = len(v)
    start_time_vector = v.rvs_normal(scale=0).project(grid, scale=0).multiply(0.25)
    pitch_vector = Vector(pitch_list[index] * np.ones(N))
    velocity_vector = (Vector(100*np.ones(N))
                        .rvs_normal(scale=10)
                        .astype(int)
                        )
    duration_vector = Vector(0.25*np.ones(N))
    sequence = Sequence(start_time_vector, pitch_vector, velocity_vector, duration_vector)
    sequence.send_to_ableton(clip)

```
