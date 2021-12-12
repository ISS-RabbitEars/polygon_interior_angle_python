import math
import matplotlib.pyplot as plt
from matplotlib import animation

fig, a=plt.subplots()
r=1
n=100

def run(frame):
    x0=1
    y0=0
    plt.clf()
    ax=plt.gca()
    ax.set_aspect(1)
    ax.set_facecolor('xkcd:black')
    for i in range(frame+4):
        x=r*math.cos(2*math.pi*i/(frame+3))
        y=r*math.sin(2*math.pi*i/(frame+3))
        plt.plot([x0,x],[y0,y],color='r')
        x0=x
        y0=y
    plt.title('$n$=%i , $\\theta$=%f\u00b0' % (frame+3,180*(1-2/(frame+3))))
ani=animation.FuncAnimation(fig,run,frames=n,interval=1000)
writervideo = animation.FFMpegWriter(fps=1)
ani.save('vani.mp4', writer=writervideo)
plt.show()
