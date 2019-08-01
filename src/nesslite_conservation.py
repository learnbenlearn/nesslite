#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 14:42:04 2019

@author: Ben
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 11:56:05 2019

@author: Ben
"""
  
mass_array = [330317.8, 95.2, 14.5, 17.2, 0.002, 0.0001073, 0.00007334, 
              0.00006196, 0.006708, 0.0002344, 0.0007368, 0.00004461, 
              0.0002930, 0.002780, 0.3]
G = 0.000118426

infile = open("snapshot_first_1k", "r")
data = infile.read()
line_list = data.splitlines()
infile.close()

x_array = []
y_array = []
z_array = []
name_array = []
x_velocity_array = []
y_velocity_array = []
z_velocity_array = []

for i in range(15):
    x_array.append(0)
    y_array.append(0)
    z_array.append(0)
    name_array.append('')
    x_velocity_array.append(0)
    y_velocity_array.append(0)
    z_velocity_array.append(0)

for i in range(15):
    templist = line_list[i].split(" ")
    x_array[i] = float(templist[1])
    y_array[i] = float(templist[2])
    z_array[i] = float(templist[3])
    name_array[i] = templist[0]
    x_velocity_array[i] = float(templist[4])
    y_velocity_array[i] = float(templist[5])
    z_velocity_array[i] = float(templist[6])

velocity_array = []

for i in range(15):
    velocity_array.append(
            x_velocity_array[i]**2 + y_velocity_array[i]**2 + z_velocity_array[i]**2)
    
# total potential energy calculation
potential_energy = 0.0
r = 0.0

for i in range(15):
    for j in range(15):
        if(i != j):
            r = ((x_array[i] - x_array[j])**2 + (y_array[i] - y_array[j])**2 + (z_array[i] - z_array[j])**2)**(1/2)
            potential_energy += G * mass_array[i] * mass_array[j] / (r)
            
# total kinetic energy calculation
kinetic_energy = 0.0

for i in range(15):
    kinetic_energy += mass_array[i] * velocity_array[i]

kinetic_energy *= 1/2

initial_total_energy = kinetic_energy + potential_energy

#angular momentum calculations
initial_x_angular_momentum = 0.0
initial_y_angular_momentum = 0.0
initial_z_angular_momentum = 0.0

for i in range(15):
    initial_x_angular_momentum += (y_array[i] * z_velocity_array[i] - z_array[i] * y_velocity_array[i]) * mass_array[i]
    initial_y_angular_momentum += (z_array[i] * x_velocity_array[i] - x_array[i] * z_velocity_array[i]) * mass_array[i]
    initial_z_angular_momentum += (x_array[i] * y_velocity_array[i] - y_array[i] * x_velocity_array[i]) * mass_array[i]

infile = open("snapshot_last_1k", "r")
data = infile.read()
line_list = data.splitlines()
infile.close()

x_array = []
y_array = []
z_array = []
name_array = []
x_velocity_array = []
y_velocity_array = []
z_velocity_array = []

for i in range(15):
    x_array.append(0)
    y_array.append(0)
    z_array.append(0)
    name_array.append('')
    x_velocity_array.append(0)
    y_velocity_array.append(0)
    z_velocity_array.append(0)

for i in range(15):
    templist = line_list[-i].split(" ")
    x_array[-i] = float(templist[1])
    y_array[-i] = float(templist[2])
    z_array[-i] = float(templist[3])
    name_array[-i] = templist[0]
    x_velocity_array[-i] = float(templist[4])
    y_velocity_array[-i] = float(templist[5])
    z_velocity_array[-i] = float(templist[6])

velocity_array = []

for i in range(15):
    velocity_array.append(
            x_velocity_array[i]**2 + y_velocity_array[i]**2 + z_velocity_array[i]**2)
    
# total potential energy calculation
potential_energy = 0.0
r = 0.0

for i in range(15):
    for j in range(15):
        if(i != j):
            r = ((x_array[i] - x_array[j])**2 + (y_array[i] - y_array[j])**2 + (z_array[i] - z_array[j])**2)**(1/2)
            potential_energy += G * mass_array[i] * mass_array[j] / (r)
            
# total kinetic energy calculation
kinetic_energy = 0.0

for i in range(15):
    kinetic_energy += mass_array[i] * velocity_array[i]

kinetic_energy *= 1/2

final_total_energy = kinetic_energy + potential_energy


final_x_angular_momentum = 0.0
final_y_angular_momentum = 0.0
final_z_angular_momentum = 0.0

for i in range(15):
    final_x_angular_momentum += (y_array[i] * z_velocity_array[i] - z_array[i] * y_velocity_array[i]) * mass_array[i]
    final_y_angular_momentum += (z_array[i] * x_velocity_array[i] - x_array[i] * z_velocity_array[i]) * mass_array[i]
    final_z_angular_momentum += (x_array[i] * y_velocity_array[i] - y_array[i] * x_velocity_array[i]) * mass_array[i]
    
print("Total Energy\n Initial Total Energy = %f\n Final Total Energy = %f\n Fractional Energy Difference = %f\n" 
      % (initial_total_energy, final_total_energy, (abs(final_total_energy - initial_total_energy)/initial_total_energy)))
print("Angular Momentum\n Initial X Angular Momentum = %f\n Initial Y Angular Momentum = %f\n Initial Z Angular Momentum = %f\n" 
      % (initial_x_angular_momentum, initial_y_angular_momentum, initial_z_angular_momentum))
print("Final X Angular Momentum = %f\n Final Y Angular Momentum = %f\n Final Z Angular Momentum = %f\n" 
      % (final_x_angular_momentum, final_y_angular_momentum, final_z_angular_momentum))
print("Fractional X Angular Momentum Difference = %f\n Fractional Y Angular Momentum Difference = %f\n Fractional Z Angular Momentum Difference = %f\n" 
      % (abs((initial_x_angular_momentum - final_x_angular_momentum)/initial_x_angular_momentum), abs((initial_y_angular_momentum - final_y_angular_momentum)/initial_y_angular_momentum), 
        abs((initial_z_angular_momentum - final_z_angular_momentum)/initial_z_angular_momentum)))
