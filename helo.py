import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def main():
    numframes = 100
    numpoints = 10
    y = np.random.random((numframes, numpoints))
    x= np.random.random((numframes, numpoints))
    
    a = [[x[i],y[i]] for i in range(numframes)]
  
    print(a,x[0],y[0])
    fig = plt.figure()
    scat = plt.scatter(x[0],y[0])
    
    ani = animation.FuncAnimation(fig, update_plot, frames= range(numframes),fargs=(a, scat))
    plt.show()

def update_plot(i, a,  scat):
    scat.set_offsets(np.transpose(a[i]))

    return scat

main()

