HEADERS = nesslite.h

default: nesslite

nesslite: $(HEADERS)
	gcc leapfrog.c particle_struct.c nesslite.c -o ../build/nesslite

clean:
	-rm -f ../build/nesslite

clean_output:
	-rm -f ../output/snapshot_first_1k
	-rm -f ../output/snapshot_last_1k
	-rm -f ../output/first_1k_snapshots/*
	-rm -f ../output/last_1k_snapshots/*
