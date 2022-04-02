import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
style.use('fivethirtyeight')

fig = plt.figure()
# Label Axis and Title
plt.xlabel('Time (s)')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Against Time\nJournal Bearing Rig')
plt.legend()

ax1 = fig.add_subplot(1,1,1)

def animate():
    x1 = []
    y1 = []
    x2 = []
    y2 = []

    updateValues('/home/pi/Ciaran/data_files/test1.csv', x1, y1)
    updateValues('/home/pi/Ciaran/data_files/test2.csv', x2, y2)

    # Define Legend
    ax1.clear()
    ax1.plot(x1, y1, label='Thermocouple 1')
    ax1.plot(x2, y2, label='Thermocouple 2')

def updateValues(path, xAxis, yAxis):
    graph_data1 = open(path, 'r').read()
    lines = graph_data1.split('\n')

    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xAxis.append(float(x))
            yAxis.append(float(y))
    
ani = animation.FuncAnimation(fig, animate(), interval=1000)
plt.show()