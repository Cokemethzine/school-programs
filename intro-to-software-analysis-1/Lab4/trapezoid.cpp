/*
Josiel Perez
CSCI-136
Minh Nguyen
print cross
*/
#include <iostream>
using namespace std;

int main(){
    int width, height;
    cout << "Please input width: " << endl;
    cin >> width;
    cout << "Please input height: " << endl;
    cin >> height;

    int spaces = 0, stars = width;
    // Formula for imposible case
    if (width-height < width/2){
        cout << "Impossible shape!" << endl;
    }
    else{
        for(int row=0; row < height; row++){// do it for every lines
            // print the number of spaces
            for(int col=0; col < spaces; col++){
                cout << " ";
            }
            for(int col=0; col < stars; col++){
                cout << "*";
            }
            cout << endl;
            spaces +=1;
            stars -=2;
        }
    }
    return 0;
}