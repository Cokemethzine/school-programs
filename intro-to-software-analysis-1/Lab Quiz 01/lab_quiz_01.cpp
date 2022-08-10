/*
Author: Josiel Perez
Course: CSCI-135
Instructor: Tong Yi
Assignment: Lab Quiz 01

I love C++: Enter an int, print that number of "I love C++" lines. 
For example, if input is 5, then print 5 such lines. Print out is case sensitive.
*/

#include <iostream>
using namespace std;


int main(){
    int i, user;
    cout << "Enter an int: ";
    cin >> user;
    for (i = 0; i < user; i++){
        cout << "I love C++" << endl;
    }
    return 0;
}