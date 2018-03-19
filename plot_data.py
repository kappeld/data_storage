import json
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation



def update_plot(i, data,  scat,time):
    time.set_text("%d ms" % (i*total_simulation_time / frames))
    scat.set_offsets(np.transpose([range(len(data[0])),data[i][...,0]]))

    return scat,


def animatedplot(fig,data1,data2):
    
    time = fig.text(0.02, 0.95, '')
    time.set_text("")
    
    plt.subplot(312)
    scat1 = plt.scatter(range(len(data1[0])),data1[0][...,0], c = data1[0][...,1])
    plt.colorbar(scat1, spacing='proportional')
    plt.ylabel("Up Neuron Group Weights")
    plt.xlabel("Time (ms)")
    plt.ylim(0,5)
    ani1 = animation.FuncAnimation(fig, update_plot, frames= range(frames),fargs=(data1, scat1,time))

    plt.subplot(313) 
    scat2 = plt.scatter(range(len(data2[0])),data2[0][...,0], c = data2[0][...,1])
    plt.colorbar(scat2, spacing='proportional')
    plt.ylabel("Down Neuron Group Weights")
    plt.xlabel("Time (ms)")
    plt.ylim(0,5)
    ani2 = animation.FuncAnimation(fig, update_plot, frames= range(frames),fargs=(data2, scat2,time))    
    
    plt.show()

    return ani2



####General Parameters####
total_simulation_time = 100
frames = 2

with open('data.txt') as json_data:
    d = json.load(json_data)
fig = plt.figure(1)
plt.subplot(311)
plt.plot(d["saving_time"],d["mean_reward"])
plt.ylabel("Mean Reward")
plt.xlabel("Time (ms)")
with open('weightsUP.txt') as json_data:
    d1 = json.load(json_data)
with open('weightsDOWN.txt') as json_data:
    d2 = json.load(json_data)
d1 = np.array(d1)
d2 = np.array(d2)

d1[:][...,1] -= np.min(d1[0][...,1])
d2[:][...,1] -= np.min(d2[0][...,1])
d11 = [d1[0][...,1] , d1[0][...,0]]
d22 = [d2[0][...,1] , d2[0][...,0]]


animatedplot(fig,d1,d2)


plt.show()
plt.close()




