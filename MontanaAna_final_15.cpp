
#include <iostream>
#include <fstream>
using namespace std;


int main(){

	ofstream outfile;
	outfile.open("final15.dat");
	float t = 0; 
	float dt = 0.1 ;
	float m = 7294.29 ;
	float q = 2 ;
	//condiciones iniciales
	float Ex;
	float Ey;
	float x = 1;
	float y = 0 ;
	float vx = 0;
	float vy = 1;   


	while(t<10){


		outfile << t << " "<< x << " " << y << endl; 
		//defino los valores de E dependiendo el tiempo 
		if (t < 3.0 ){
			Ex = 0; 
			Ey = 0;
		}
		if ( 3.0 > t > 7.0){
			Ex = 0; 
			Ey = 3;
		}
		if (t < 3.0 ){
			Ex = 0; 
			Ey = 0;
		}

		x = x + (1.0/2.0)*dt*vx;
		vx = vx + dt*((q*Ex)/m);
		x = x + (1.0/2.0)*dt*vx;

		y = y + (1.0/2.0)*dt*vy;
		vy = vy + dt*((q*Ex)/m);
		y = y + (1.0/2.0)*dt*vy;


		t = t + dt ;
		 

	}


	outfile.close();

	return 0;





}