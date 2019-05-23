MontanaAna_final_15.pdf: MontanaAna_final_15.py final15.dat
	python MontanaAna_final_15.py

final15.dat: MontanaAna_final_15.x
	./MontanaAna_final_15.x

MontanaAna_final_15.x: MontanaAna_final_15.cpp
	g++ MontanaAna_final_15.cpp -o MontanaAna_final_15.x 
