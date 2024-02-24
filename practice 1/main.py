import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

group = {'Student1': {'pr1': 1, 'pr2': 2, 'pr3': 3},
         'Student2': {'pr1': 2, 'pr2': 3, 'pr3': 4},
         'Student3': {'pr1': 3, 'pr2': 4, 'pr3': 5},
         }

res = {}
for i in group:
    res[i] = [sum(group[i].values()) / len(group[i])]

df = (pd.DataFrame(res)
      .transpose()
      .rename(columns={0: 'scores'}))

print(df)

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

plt.plot(x, y, label='sin(x)')
plt.xlabel('x')

plt.ylabel('sinx(x)')
plt.title('Графік sin(x)')

plt.legend()

plt.grid(True)
plt.show()


import seaborn as s

# Use the standard design
s.set_theme()

# Bring up the testing information
tips = s.load_dataset("tips")

# Construct a visual picture
s.relplot(
    data=tips,
    x="total_bill", y="tip", col="time",
    hue="smoker", style="smoker", size="size",
)


import seaborn as sns
import matplotlib.pyplot as plt

# loading dataset
data = sns.load_dataset("iris")

sns.scatterplot(x='sepal_length', y='sepal_width', data=data)
plt.show()
