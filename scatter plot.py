import sys
import matplotlib

matplotlib.use('TkAgg')

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot(kind='scatter', x='Duration', y='Calories')

plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
