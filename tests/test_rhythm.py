from orthophonic.base import Sine_Zeros
import numpy as np

N = 16
for m in [4, 5, 7]:
    v = Sine_Zeros(m, N)
    print(f"{m}, {N}:")
    print(f"before projection: {v}")
    v2 = v.project(np.arange(16), scale=0).astype(int)
    print(f"after projection: {v2}")

