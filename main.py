import numpy as np
import pandas as pd
import matplotlib as plt

dzieci = {'liczba': [123,444,333],
          'rok': ['2010', '2015','2020']}
df = pd.DataFrame(dzieci)
print(df)
plt.show()