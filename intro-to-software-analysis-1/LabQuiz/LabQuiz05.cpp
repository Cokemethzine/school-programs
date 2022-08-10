#include <iostream>
#include <fstream>
using namespace std;

int main(){
    string color;
    ifstream myfile("data.txt");
    while (getline (myfile, color))
    {
        cout << color << endl;
    }
    myfile.close();
    
}