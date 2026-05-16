import matplotlib.pyplot as plt
import numpy as np
time=[0,2,4,6,8,10,12]
tide=[1.2,2.5,3.8,2.9,1.5,2.7,4.0]

mean_level= np.mean(tide)

plt.plot(time, tide, marker='o',
         label="Tide level")
plt.axhline(mean_level,color='red', linestyle='--', label="Mean Sea Level")

plt.title("Tidal Varation with Mean Sea Level")
plt.xlabel("Time (hours)")
plt.ylabel("Sea level (m)")
plt.grid()
plt.legend()

plt.savefig("tide_mean_level.png")
plt.show()
