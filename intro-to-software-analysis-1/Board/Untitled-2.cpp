#include <iostream>
using namespace std;

int main(){
    int size = 26;
    string *data = new string[size];
    cout << "Enter " << 26 << "strings" << endl;
    for(int i = 0; i< size; i++){
        getline(cin,data[i]);
    }
    string longest = data[0];
    for(int i = 0; i<size;i++)
        if(data[i].length() > longest.length())
            longest = data[i];
    cout << "longest string: " << longest << endl;
}