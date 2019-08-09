
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 11:56:05 2019

@author: Ben
"""
import matplotlib.pyplot as plt

infile = open("../output/snapshot_first_1k", "r")
data = infile.read()
line_list = data.splitlines()
infile.close()

x_array = []
y_array = []

for i in range(15):
    column1 = []
    column2 = []
    for m in range(1000):
        column1.append(0)
        column2.append(0)
    x_array.append(column1)
    y_array.append(column2)

j = 0
k = 0

for i in range(15000):
    templist = line_list[i].split(" ")
    x_array[j][k] = float(templist[1])
    y_array[j][k] = float(templist[2])
    
    if(j < 14):
        j += 1
    else:
        j = 0
        k += 1
        
x_graph = []
y_graph = []

for j in range(1000):
    for i in range(15):
        x_graph.append(x_array[i][j] - x_array[0][j])
        y_graph.append(y_array[i][j] - y_array[0][j])
        
    plt.plot(x_graph, y_graph, 'k.', (x_array[14][j] - x_array[0][j]),
             (y_array[14][j] - y_array[0][j]), 'g.')
    plt.xlim(-2e2, 2e2)
    plt.ylim(-2e2, 2e2)
    plt.text(1e2, -2e2, "Time: %.2f yrs" % (2.94 * j))
    plt.axis('off')
    fig = plt.gcf()
    if(j < 10):
        fig.savefig('%s/snapshot_000%d.png' % ("../output/first_1k_snapshots", j), dpi=200)
    elif(j < 100):
        fig.savefig('%s/snapshot_00%d.png' % ("../output/first_1k_snapshots", j), dpi=200)
    elif(j < 1000):
        fig.savefig('%s/snapshot_0%d.png' % ("../output/first_1k_snapshots", j), dpi=200)
    else:
        fig.savefig('%s/snapshot_%d.png' % ("../output/first_1k_snapshots", j), dpi=200)
    plt.clf()

    x_graph = []
    y_graph = []
  
infile = open("../output/snapshot_last_1k", "r")
data = infile.read()
line_list = data.splitlines()
infile.close()

x_array = []
y_array = []

for i in range(15):
    column1 = []
    column2 = []
    for m in range(1000):
        column1.append(0)
        column2.append(0)
    x_array.append(column1)
    y_array.append(column2)

j = 0
k = 0

for i in range(15000):
    templist = line_list[i].split(" ")
    x_array[j][k] = float(templist[1])
    y_array[j][k] = float(templist[2])
    
    if(j < 14):
        j += 1
    else:
        j = 0
        k += 1
        
x_graph = []
y_graph = []

for j in range(1000):
    for i in range(15):
        x_graph.append(x_array[i][j] - x_array[0][j])
        y_graph.append(y_array[i][j] - y_array[0][j])
        
    plt.plot(x_graph, y_graph, 'k.', (x_array[14][j] - x_array[0][j]),
             (y_array[14][j] - y_array[0][j]), 'g.')
    plt.xlim(-2e2, 2e2)
    plt.ylim(-2e2, 2e2)
    plt.text(1e2, -2e2, "Time: %.2f yrs" % (9997060 + 2.94 * j))
    plt.axis('off')
    fig = plt.gcf()
    if(j < 10):
        fig.savefig('%s/snapshot_000%d.png' % ("../output/last_1k_snapshots", j), dpi=200)
    elif(j < 100):
        fig.savefig('%s/snapshot_00%d.png' % ("../output/last_1k_snapshots", j), dpi=200)
    elif(j < 1000):
        fig.savefig('%s/snapshot_0%d.png' % ("../output/last_1k_snapshots", j), dpi=200)
    else:
        fig.savefig('%s/snapshot_%d.png' % ("../output/last_1k_snapshots", j), dpi=200)
    plt.clf()

    x_graph = []
    y_graph = []
