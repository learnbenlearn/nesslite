HEADERS = nesslite.h

default: nesslite

nesslite: $(HEADERS)
	gcc leapfrog.c particle_struct.c nesslite.c -o ../build/nesslite

clean:
	-rm -f ../build/nesslite
