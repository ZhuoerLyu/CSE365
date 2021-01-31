c_program: c_program.o
	gcc c_program.o -o c_program
c_program.o: c_program.c
	gcc -c c_program.c 
clean: 
	rm *.o c_program
