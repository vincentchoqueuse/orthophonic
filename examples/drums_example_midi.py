from orthophonic.base import Vector, Sine_Zeros
from orthophonic.utils import generate_grid, save_to_midi
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

# sorte list of note
note_list = []

for index, v in enumerate(v_list):
    N = len(v)
    start_time_vector = v.project(grid, scale=0).multiply(0.25)
    pitch_vector = Vector(pitch_list[index] * np.ones(N))
    velocity_vector = (Vector(100*np.ones(N))
                        .rvs_normal(scale=10)
                        .astype(int)
                        )
    duration_vector = Vector(0.25*np.ones(N))
    sequence = Sequence(start_time_vector, pitch_vector, velocity_vector, duration_vector)
    note_list += sequence.get_notes()
    
# export to midi file
save_to_midi(note_list, filename="data.mid")
