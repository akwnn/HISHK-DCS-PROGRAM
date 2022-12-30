import matplotlib.pyplot as plt
import pandas as pd
from itertools import count
from matplotlib.animation import FuncAnimation

df = pd.read_excel('excel_files/HK_annual_temp.xlsx')
x = []
y = []

fig,ax =plt.subplots()
ax.plot(x,y)

counter = count(0,1)
def update(i):
    index= next(counter)
    x.append(df.iloc[index,0])
    y.append(df.iloc[index,1])
    plt.cla()
    ax.plot(x,y)
    plt.title("Annual Mean Temp in HK")
    plt.xlabel("Year")
    plt.ylabel("Temperature °C")
    
anim =FuncAnimation(fig=fig, func=update, interval=200,)
plt.show()



