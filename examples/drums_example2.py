from orthophonic.base import Vector, Sine_Zeros
from orthophonic.utils import generate_grid, create_clip
from orthophonic.sequence import Sequence
import live
import numpy as np


clip_index = 1
track_index = 0
sigma_time = 0.4
repeat = 4

# generate master grid
grid = generate_grid(N=16, repeat=repeat)

# custom euclidean rhythms
v0 = Sine_Zeros(3, 16, repeat=repeat)
v1 = Sine_Zeros(6, 16, repeat=repeat).add(2)
v2 = Sine_Zeros(2, 16, repeat=repeat).add(4)
v3 = Sine_Zeros(5 , 16, repeat=repeat).add(3)
v4 = Sine_Zeros(7, 16, repeat=repeat).add(2)
v5 = Sine_Zeros(7, 16, repeat=repeat).add(2)
v6 = Sine_Zeros(12, 16, repeat=repeat).add(2)
v_list = [v0, v1, v2, v3, v4, v5]

# generate list of pitch. Each pitch correspond to a note of a the drumkit
pitch_list = np.array([36, 40, 43, 44, 42, 37]) + 3*12

# connect to Ableton / create clip
set = live.Set(scan=True)
clip = create_clip(set, track_index, clip_index, 16, erase=True)

for index, v in enumerate(v_list):
    N = len(v)
    start_time_vector = v.project(grid, scale=0).multiply(0.25)
    pitch = pitch_list[index] * np.ones(N)
    pitch_vector = Vector(pitch)
    if index == 6:
        pitch_vector = pitch_vector.rvs_normal(scale=4)
    velocity_vector = Vector(100*np.ones(N)).rvs_normal(scale=2).astype(int)
    duration_vector = Vector(0.25*np.ones(N))

    sequence = Sequence(start_time_vector, pitch_vector, velocity_vector, duration_vector)
    sequence.send_to_ableton(clip)