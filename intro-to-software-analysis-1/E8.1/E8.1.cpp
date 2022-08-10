/*
Josiel Perez
CSCI-135
Tong Yi
Making a program that carries out the following tasks
*/

#include <iostream>
#include <fstream>
using namespace std;

int main(){
    fstream myfile;
    myfile.open("hello.txt");
    myfile << "Hello, World!" << endl;
    myfile.close();
    
    string sentence;

    myfile.open("hello.txt");
    getline(myfile, sentence);
    cout << sentence << endl;
    myfile.close();
    
    return 0;
}