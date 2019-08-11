"""
Created on Thu May  2 11:56:05 2019

@author: Ben
"""
import matplotlib.pyplot as plt
import numpy as np

def plotter(filename, numsnapshot):
    # get filename and read data
    infile = open("%s" % filename, "r")
    data = infile.read()
    line_list = data.splitlines()
    infile.close()
    
    # set up iteration variables
    x_array = np.zeros((15, (len(line_list) // 15)))
    x_array = np.zeros((15, (len(line_list) // 15)))
    y_array = np.zeros((15, (len(line_list) // 15)))
    j = 0
    k = 0
    current_snapshot = numsnapshot

    # add position values to arrays
    for i in range(len(line_list)):
        templist = line_list[i].split(" ")
        x_array[j][k] = float(templist[1])
        y_array[j][k] = float(templist[2])
    
        if(j < 14):
            j += 1
        else:
            j = 0
            k += 1
        
    x_graph = np.zeros(15)
    y_graph = np.zeros(15)
        
    # plot positions of all bodies at given timestep and save figure; reset
    # iteration variables
    for j in range(len(line_list) // 15):
        for i in range(15):
            x_graph[i] = x_array[i][j] - x_array[0][j]
            y_graph[i] = y_array[i][j] - y_array[0][j]
        
        plt.plot(x_graph[0:14], y_graph[0:14], 'k.', x_graph[14], y_graph[14], 'g.')
        plt.xlim(-15e1, 15e1)
        plt.ylim(-15e1, 15e1)
        plt.text(1e2, -15e1, "Time: %d yrs" % (2940 * current_snapshot))
        plt.axis('off')
        fig = plt.gcf()
        if(current_snapshot < 10):
            fig.savefig('%s/snapshot_000%d.png' % ("../output/snapshots/", 
                                                   current_snapshot), dpi=200)
        elif(current_snapshot < 100):
            fig.savefig('%s/snapshot_00%d.png' % ("../output/snapshots/", 
                                                  current_snapshot), dpi=200)
        elif(current_snapshot < 1000):
            fig.savefig('%s/snapshot_0%d.png' % ("../output/snapshots/", 
                                                 current_snapshot), dpi=200)
        else:
            fig.savefig('%s/snapshot_%d.png' % ("../output/snapshots/", 
                                                current_snapshot), dpi=200)
        plt.clf()
        x_graph = np.zeros(15)
        y_graph = np.zeros(15)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
        current_snapshot += 1

def main():
    plotter("../output/snapshotfile_001", 0)
    plotter("../output/snapshotfile_002", 1000)
    plotter("../output/snapshotfile_003", 2000)
    plotter("../output/snapshotfile_004", 3000)

main()
