/*
Josiel Perez
CSCI-136
Minh Nguyen
print checkboard
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
            if ((i+j)%2 == 0){ //  both row and col are odd or even at the same time.
                cout << "*";
            }
            else{
                cout << " ";
            }
        }
        cout << endl;
    }
    return 0;
}