import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    graph_data1 = open('/home/pi/Ciaran/data_files/test1.csv', 'r').read()
    lines = graph_data1.split('\n')
    x1 = []
    y1 = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            x1.append(float(x))
            y1.append(float(y))
    ax1.clear()
    
    
    
    graph_data2 = open('/home/pi/Ciaran/data_files/test2.csv', 'r').read()
    lines = graph_data2.split('\n')
    x2 = []
    y2 = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            x2.append(float(x))
            y2.append(float(y))
    ax1.clear()
    ax1.plot(x1, y1, label='Thermocouple 1')
    ax1.plot(x2, y2, label='Thermocouple 2')
    

    plt.xlabel('Time (s)')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Against Time\nJournal Bearing Rig')
    plt.legend()
    
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()