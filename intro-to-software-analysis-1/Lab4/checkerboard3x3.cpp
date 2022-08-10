/*
Josiel Perez
CSCI-136
Minh Nguyen
print cross
*/
#include <iostream>
using namespace std;

int main(){
    // variable
    int width, height;
    cout << "Please input width: " << endl;
    cin >> width;
    cout << "Please input height: " << endl;
    cin >> height;

    for(int row=0; row < height; row++){// do it for every lines
        for (int col = 0; col < width; col++){
            if ((row/3+col/3)%2 == 0){
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