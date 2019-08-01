//
//  leapfrog.c
//  
//
//  Created by Benjamin Learn on 4/23/19.
//

#include <stdio.h>
#include "nesslite.h"
#include <math.h>

/* functions to perform leap-frog method for position and velocity calculation to completely describe particle in 6-dimensional space */

const double h = 2.94; // 1/10 of Saturn's orbital period in years
const double epsilon_cubed = 10e-6;
const double G = 0.000118426; // AU^3 M_earth^-1 y^-2

double calculateR(int index1, int index2){
    double r_2 = pow((solarSystemObjects[index1].xposition_n - solarSystemObjects[index2].xposition_n), 2) + pow((solarSystemObjects[index1].yposition_n - solarSystemObjects[index2].yposition_n), 2) + pow((solarSystemObjects[index1].zposition_n - solarSystemObjects[index2].zposition_n), 2);
    double r_3 = pow(sqrt(r_2), 3);
    return r_3;
}

/* equations of motion:

dr_i/dt = v_i

 dv_i/dt = a_i = sum_{j != i} G m_j / (mag(r_i - r_j)^2 + epsilon^2) * rhat_{i,j} = sum_{j != i} G m_j / (mag(r_i - r_j)^3 + epsilon^2) * r_x,y,z*/

/* position evolution equation: xn1 = xn + vnew * h */
void xpositionLF(int index){
    solarSystemObjects[index].xposition_n1 = solarSystemObjects[index].xposition_n + solarSystemObjects[index].xvelocity_newhalf * h;
}
void ypositionLF(int index){
    solarSystemObjects[index].yposition_n1 = solarSystemObjects[index].yposition_n + solarSystemObjects[index].yvelocity_newhalf * h;
}
void zpositionLF(int index){
    solarSystemObjects[index].zposition_n1 = solarSystemObjects[index].zposition_n + solarSystemObjects[index].zvelocity_newhalf * h;
}

/* velocity evolution equation: vnew = vold + F(xn) * h / m */
void xvelocityLF(int index){
    double F = 0;
    double r_3 = 0;
    int i;
    for(i=0; i<15; i++){
        if(i != index){
            r_3 = calculateR(index, i);
            F += solarSystemObjects[i].mass * (solarSystemObjects[i].xposition_n - solarSystemObjects[index].xposition_n) / (r_3 + epsilon_cubed);
        }
    }
    solarSystemObjects[index].xvelocity_newhalf = solarSystemObjects[index].xvelocity_oldhalf + G * F * h;
}
void yvelocityLF(int index){
    double F = 0;
    double r_3 = 0;
    int i;
    for(i=0; i<15; i++){
        if(i != index){
            r_3 = calculateR(i, index);
            F += solarSystemObjects[i].mass * (solarSystemObjects[i].yposition_n - solarSystemObjects[index].yposition_n) / (r_3 + epsilon_cubed);
        }
    }
    solarSystemObjects[index].yvelocity_newhalf = solarSystemObjects[index].yvelocity_oldhalf + G * F * h;
}
void zvelocityLF(int index){
    double F = 0;
    double r_3 = 0;
    int i;
    for(i=0; i<15; i++){
        if(i != index){
            r_3 = calculateR(i, index);
            F += solarSystemObjects[i].mass * (solarSystemObjects[i].zposition_n - solarSystemObjects[index].zposition_n) / (r_3 + epsilon_cubed);
        }
    }
    solarSystemObjects[index].zvelocity_newhalf = solarSystemObjects[index].zvelocity_oldhalf + G * F * h;
}
