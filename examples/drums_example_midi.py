from orthophonic.base import Vector, Sine_Zeros
from orthophonic.utils import generate_grid, save_to_midi
from orthophonic.sequence import Sequence
import numpy as np
import live

# initial parameters
track_index = 0
clip_index = 0
track_index = 0
sigma_time = 0.4
repeat = 4

# generate master grid
grid = generate_grid(N=16, repeat=repeat)

# custom euclidean rhythms
v_list = [
    Sine_Zeros(3, 16, repeat=repeat),               # kick pattern
    Sine_Zeros(2, 16, repeat=repeat).add(4),        # snare pattern
    Sine_Zeros(5, 16, repeat=repeat).add(3),
    Sine_Zeros(7, 16, repeat=repeat).add(1),
    Sine_Zeros(9, 16, repeat=repeat).add(2),
    Sine_Zeros(5, 16, repeat=repeat).add(1)
]

# generate list of pitch. Each pitch correspond to a note of a the drumkit
pitch_list = [36, 41, 44, 57, 49, 55]

# sort list of notes
note_list = []

for index, v in enumerate(v_list):
    pitch = pitch_list[index]
    start_time_vector = v.rvs_normal(scale=0).project(grid, scale=0).multiply(0.25)
    pitch_vector = Vector(pitch) 
    velocity_vector = Vector(100).resize(len(v)).rvs_normal(scale=10)
    duration_vector = Vector(0.25)
    sequence = Sequence(start_time_vector, pitch_vector, velocity_vector, duration_vector)
    note_list += sequence.get_notes()
    
# export to midi file
save_to_midi(note_list, filename="data.mid")
