from orthophonic.sequence import Sequence
from orthophonic.base import Vector, Sine_Zeros
from orthophonic.utils import generate_scale, generate_grid, create_clip
import numpy as np
import live

# intial parameters
theta = 1/6  # minor grid (see paper)
repeat = 4    
clip_index = 1
track_index = 3

# generate scale from projection and master grid
scale = generate_scale(root=40, theta=theta)
grid = generate_grid(N=16, repeat=repeat)

# pitch progression (numpy spirit)
transpose = 12
pitch_vect = np.array([40-24, 40-12, 42, 46]) + transpose
progression = np.array([0, -2, -4, -2])

# generate rhythms using Custom Euclidean Rhythm
v1 = Sine_Zeros(2, 16, repeat=repeat)
v2 = Sine_Zeros(4, 16, repeat=repeat).add(3)
v3 = Sine_Zeros(4, 16, repeat=repeat).add(3)
v4 = Sine_Zeros(5, 16, repeat=repeat).add(5)
v_list = [v1, v2, v3, v4]

# connect to Ableton / create clip
set = live.Set(scan=True)
clip = create_clip(set, track_index, clip_index, 16, erase=True)

for index, v in enumerate(v_list):
    start_time_vector = v.project(grid, scale=0).multiply(0.25)
    N = len(start_time_vector)
    pitch = pitch_vect[index] * np.ones(int(N/repeat))
    pitch_vector = Vector(progression).direct_sum(Vector(pitch)).project(scale)
    velocity_vector = Vector(100*np.ones(N)).rvs_normal(scale=0).astype(int)
    duration_vector = Vector(1.*np.ones(N))

    sequence = Sequence(start_time_vector, pitch_vector, velocity_vector, duration_vector)
    sequence.send_to_ableton(clip)

