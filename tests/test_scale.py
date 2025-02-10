from orthophonic.base import Sine_Zeros
import numpy as np

N = 12
M = 7
repeat = 12
root_note = 40%12

m_vect = np.arange(M) 
theta_vect = (-1/2) + 0.999*m_vect/(M-1)
for theta in theta_vect:
    v = (Sine_Zeros(M, N, theta=theta, repeat=repeat)
            .project(np.arange(repeat*N))
            .add(root_note - 12)
            .clip()
            .astype(int)
        )
    print(f"theta={theta}:")
    print(f"{v}")

