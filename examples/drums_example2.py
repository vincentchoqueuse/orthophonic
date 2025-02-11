from orthophonic.base import Vector, Sine_Zeros
from orthophonic.utils import generate_grid, create_clip
from orthophonic.sequence import Sequence
import live
import numpy as np

# initial parameters
clip_index = 1
track_index = 0
sigma_time = 0.4
repeat = 4

# generate master grid
grid = generate_grid(N=16, repeat=repeat)

# custom euclidean rhythms
v_list = [
    Sine_Zeros(4, 16, repeat=repeat),               # kick pattern
    Sine_Zeros(2, 16, repeat=repeat).add(4),       # snare pattern
    Sine_Zeros(5, 16, repeat=repeat).add(2),
    Sine_Zeros(7, 16, repeat=repeat).add(1),
    Sine_Zeros(11, 16, repeat=repeat).add(2),
    Sine_Zeros(13, 16, repeat=repeat).add(1)
]

# generate list of pitch. Each pitch correspond to a note of a the drumkit
pitch_list = [36, 41, 44, 52, 61, 55]

# connect to Ableton / create clip
set = live.Set(scan=True)
clip = create_clip(set, track_index, clip_index, 16, erase=True)

for index, v in enumerate(v_list[:6]):
    pitch = pitch_list[index]
    start_time_vector = v.project(grid, scale=0).multiply(0.25)
    pitch_vector = Vector(pitch)
    velocity_vector = Vector(100).rvs_normal(scale=2)
    duration_vector = Vector(0.25)

    sequence = Sequence(start_time_vector, pitch_vector, velocity_vector, duration_vector)
    sequence.send_to_ableton(clip)