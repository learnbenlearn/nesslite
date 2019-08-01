HEADERS = nesslite.h

default: nesslite

nesslite: $(HEADERS)
	mkdir ../build
	mkdir ../output
	mkdir ../output/first_1k_snapshots/
	mkdir ../output/last_1k_snapshots/
	gcc leapfrog.c particle_struct.c nesslite.c -o ../build/nesslite

clean:
	-rm -r ../build/

clean_output:
	-rm -r ../output/
