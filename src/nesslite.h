//
//  nesslite.h
//  
//
//  Created by Benjamin Learn on 4/22/19.
//

#ifndef nesslite_h
#define nesslite_h

#include <stdio.h>
#include <math.h>

/* functions from leapfrog.c */
void xpositionLF(int index);
void ypositionLF(int index);
void zpositionLF(int index);
void xvelocityLF(int index);
void yvelocityLF(int index);
void zvelocityLF(int index);

typedef struct {
    char *name;
    double sm_axis;
    double mass;
    double xposition_n;
    double yposition_n;
    double zposition_n;
    double xposition_n1;
    double yposition_n1;
    double zposition_n1;
    double xvelocity_oldhalf;
    double yvelocity_oldhalf;
    double zvelocity_oldhalf;
    double xvelocity_newhalf;
    double yvelocity_newhalf;
    double zvelocity_newhalf;
}Particle;

extern Particle solarSystemObjects[15];

void structCreator();

#endif /* nesslite_h */
