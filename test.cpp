#include <iostream>
#include <fstream> 
using namespace std;
int main(){
     //Fucntion is Y=X^3
    // Creation of ofstream class object 
    ofstream fout; 
    
    fout.open("data.txt");   
    
    // Execute a loop If f
    int y;
    for(int x=0; x<25;x++){
        y=(x*x);
        //getline(y, line);
        fout<<y<<" "<<x<<endl; 
    }

    // Close the File 
    fout.close(); 
    return 0;
}


    