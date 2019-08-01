//
//  nesslite.c
//  
//
//  Created by Benjamin Learn on 4/22/19.
//

#include "nesslite.h"
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(){
    /* iteration index variables */
    int i, j;
    
    /* snapshot output file */
    char snapshot_file_1[18] = "snapshot_first_1k";
    char snapshot_file_2[17] = "snapshot_last_1k";
    FILE *fp;
    FILE *gp;
    
    /* running for 10 million years with timestep of 2.94 years -> 3,401,360 time steps */
    for(i=0; i<3401360; i++){ //840337
        /* evolve each particle for each timestep */
        /* first velocity */
        for(j=0; j<15; j++){
            xvelocityLF(j);
            yvelocityLF(j);
            zvelocityLF(j);
        }
        
        /* next position */
        for(j=0; j<15; j++){
            xpositionLF(j);
            ypositionLF(j);
            zpositionLF(j);
        }
        
        /* output all current data to snapshot file */
        if(i < 1000){
            fp = fopen(snapshot_file_1, "a");
            for(j=0; j<15; j++){
                /* write output */
                fprintf(fp, "%s %lf %lf %lf %lf %lf %lf \n", solarSystemObjects[j].name, solarSystemObjects[j].xposition_n1, solarSystemObjects[j].yposition_n1, solarSystemObjects[j].zposition_n1, solarSystemObjects[j].xvelocity_newhalf, solarSystemObjects[j].yvelocity_newhalf, solarSystemObjects[j].zvelocity_newhalf);
            }
            fclose(fp);
        }
        else if((i < 3401360) && (i >= 3400360)){
            gp = fopen(snapshot_file_2, "a");
            for(j=0; j<15; j++){
                /* write output */
                fprintf(gp, "%s %lf %lf %lf %lf %lf %lf \n", solarSystemObjects[j].name, solarSystemObjects[j].xposition_n1, solarSystemObjects[j].yposition_n1, solarSystemObjects[j].zposition_n1, solarSystemObjects[j].xvelocity_newhalf, solarSystemObjects[j].yvelocity_newhalf, solarSystemObjects[j].zvelocity_newhalf);
            }
            fclose(gp);
        }
        
        /* then update all position and velocity variables */
        for(j=0; j<15; j++){
            solarSystemObjects[j].xposition_n = solarSystemObjects[j].xposition_n1;
            solarSystemObjects[j].yposition_n = solarSystemObjects[j].yposition_n1;
            solarSystemObjects[j].zposition_n = solarSystemObjects[j].zposition_n1;
        }
        for(j=0; j<15; j++){
            solarSystemObjects[j].xvelocity_oldhalf = solarSystemObjects[j].xvelocity_newhalf;
            solarSystemObjects[j].yvelocity_oldhalf = solarSystemObjects[j].yvelocity_newhalf;
            solarSystemObjects[j].zvelocity_oldhalf = solarSystemObjects[j].zvelocity_newhalf;
        }
        
        if(i % 100000 == 0){
            printf("Timestep: %d\n", i);
        }
    }
}
