#include <iostream>
using namespace std;

int main(){
    string name;
    int length;

    
    cout << "Enter phrase: ";
    getline(cin,name);
    length = name.length();

    for (int i = 1; i <= length; i++)
        cout << name.substr(0,i) << endl;
    
    for (int i = length - 1; i > 0; i--)
        cout << name.substr(0,i) << endl;


}