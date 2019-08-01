**nesslite**

nesslite is a rudimentary leapfrog N-body code that I, Ben Learn, created in the spring of 2019. nesslite simulates a system that includes the Sun, the gas giant planets (excluding Jupiter), large Kuiper Belt Objects, and a theoretical Planet Nine in order to observe the effect of Planet Nine on the solar system. Planet Nine in this version of nesslite is a 0.3 Earth mass body with a semi-major axis of 75 AU. The algorithm is far from perfect; in particular, it has lots of trouble conserving angular momentum. I plan on fixing this and other issues in future commits.

**File List and Run Commands**

nesslite source files:  
src/leapfrog.c  
src/nesslite.c  
src/particle_struct.c  
src/nesslite.h  
src/Makefile  

Run by:  
make  
./nesslite (must be in build directory)

Files for analyzing nesslite simulations:  
src/nesslite\_grapher.py *(produces snapshots of the first and last 1,000 timesteps of the simulation in output/first_1k_snapshots/ and output/last_1k_snapshots/, respectively)*  
src/nesslite\_conservation.py *(calculates initial, final, and fractional difference for total energy and angular momentum in the x, y, and z directions for the simulation)*

Run by:  
python3.6 nesslite\_grapher.py *Note: must have matplotlib installed.*  
python3.6 nesslite\_conservation.py

Commands to make videos of nesslite simulation screenshots:  
ffmpeg -r 60 -f image2 -s 1920x1080 -i last\_1k\_snapshots/snapshot\_%04d.png -pix\_fmt yuv420p last\_1k.mp4

ffmpeg -r 60 -f image2 -s 1920x1080 -i first\_1k\_snapshots/snapshot\_%04d.png -pix\_fmt yuv420p first\_1k.mp4

*Note: Must have ffmpeg installed; command should be run in output directory.*

**Movie Example**  
Below is an example of a short movie from this nesslite simulation.
