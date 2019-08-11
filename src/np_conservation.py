"""
Created on Fri May  3 14:42:04 2019

@author: Ben
"""
import numpy as np

# global constants for mass of each variable and gravitational constant
mass_array = [330317.8, 95.2, 14.5, 17.2, 0.002, 0.0001073, 0.00007334, 
              0.00006196, 0.006708, 0.0002344, 0.0007368, 0.00004461, 
              0.0002930, 0.002780, 0.3]
G = 0.000118426

def conservation(filename, firstlast):
    # read file
    infile = open("%s" % filename, "r")
    data = infile.read()
    line_list = data.splitlines()
    infile.close()
    
    # arrays for calculations
    x_array = np.zeros(15)
    y_array = np.zeros(15)
    z_array = np.zeros(15)
    name_array = []
    x_velocity_array = np.zeros(15)
    y_velocity_array = np.zeros(15)
    z_velocity_array = np.zeros(15)
    
    # populate name array with placeholders
    for i in range(15):
        name_array.append('')

    # if firstlast = 0, we're calculating initial values, start from the top
    # of the first snapshot file
    # if firstlast = 1, we're calculating final values, start 15 lines from the
    # bottom of the final snapshot file
    # populate lists
    for i in range(15):
        if(firstlast == 0):    
            templist = line_list[i].split(" ")
        else:
            templist = line_list[(len(line_list) + i - 15)].split(" ")
        x_array[i] = float(templist[1])
        y_array[i] = float(templist[2])
        z_array[i] = float(templist[3])
        name_array[i] = templist[0]
        x_velocity_array[i] = float(templist[4])
        y_velocity_array[i] = float(templist[5])
        z_velocity_array[i] = float(templist[6])

    # calculate velocity values    
    velocity_array = np.zeros(15)
    for i in range(15):
        velocity_array[i] = (x_velocity_array[i]**2 + y_velocity_array[i]**2 
                              + z_velocity_array[i]**2)
    
    # total potential energy calculation
    potential_energy = 0.0
    r = 0.0
    for i in range(15):
        for j in range(15):
            if(i != j):
                r = ((x_array[i] - x_array[j])**2 + (y_array[i] - 
                     y_array[j])**2 + (z_array[i] - z_array[j])**2)**(1/2)
                potential_energy += G * mass_array[i] * mass_array[j] / (r)
            
    # total kinetic energy calculation
    kinetic_energy = 0.0
    for i in range(15):
        kinetic_energy += mass_array[i] * velocity_array[i]
    kinetic_energy *= 1/2

    # total energy
    total_energy = kinetic_energy + potential_energy

    # angular momentum calculations
    x_angular_momentum = 0.0
    y_angular_momentum = 0.0
    z_angular_momentum = 0.0
    for i in range(15):
        x_angular_momentum += (y_array[i] * z_velocity_array[i] - z_array[i] * 
                               y_velocity_array[i]) * mass_array[i]
        y_angular_momentum += (z_array[i] * x_velocity_array[i] - x_array[i] * 
                               z_velocity_array[i]) * mass_array[i]
        z_angular_momentum += (x_array[i] * y_velocity_array[i] - y_array[i] * 
                               x_velocity_array[i]) * mass_array[i]
    
    # total angular momentum
    total_angular_momentum = (x_angular_momentum**2 + y_angular_momentum**2 + 
                              z_angular_momentum**2)**(1/2)
    
    return total_energy, total_angular_momentum

def main():
    # get initial and final energy and angular momentum values
    ini_energy, ini_ang_momentum = conservation("../output/snapshotfile_001", 0)
    fin_energy, fin_ang_momentum = conservation("../output/snapshotfile_004", 1)
    
    # output conservation values
    print("Total Energy\n Initial Total Energy = %f\n Final Total Energy = %f" 
          % (ini_energy, fin_energy))
    print(" Fractional Energy Difference = %f\n" 
          % (abs(fin_energy - ini_energy)/ini_energy))
    print("Angular Momentum\n Initial Angular Momentum = %f" 
          % ini_ang_momentum)
    print(" Final Angular Momentum = %f\n Fractional Angular Momentum Difference = %f\n" 
          % (fin_ang_momentum, abs((ini_ang_momentum - fin_ang_momentum)/ini_ang_momentum)))

main()
