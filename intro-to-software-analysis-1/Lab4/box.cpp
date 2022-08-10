/*
Josiel Perez
CSCI-136
Minh Nguyen
print size rectangle with asterisks
*/
#include <iostream>
using namespace std;

int main(){
    //variables
    int width, height;
    cout << "Please input width: " << endl;
    cin >> width;
    cout << "Please input height: " << endl;
    cin >> height;
    // we need to do do this 5 height times
    for (int i = 0; i < height; i++){
        // print out a lint od width stars.
        for (int j = 0; j < width; j++)
        {
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}