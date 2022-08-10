/*
Josiel Perez
CSCI-136
Minh Nguyen
print cross
*/
#include <iostream>
using namespace std;

int main(){
    //variables
    int size;
    cout << "Please input size: " << endl;
    cin >> size;
    // 
    for (int i = 0; i < size; i++){
        for (int j = 0; j < size; j++){
            if (i == j or i+j == size-1){ 
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