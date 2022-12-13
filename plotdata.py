import sys
import matplotlib
import tkinter

matplotlib.use('TkAgg')

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot()

plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
