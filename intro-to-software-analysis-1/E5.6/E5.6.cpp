/*
Josiel Perez
CSCI-135
Tong Yi
Making a function that returns a the middle character in a str
*/
#include <iostream>
using namespace std;

string middle(string str);

/*int main(){
    string str = "";
    cin >> str;

    cout << middle(str);
}
*/

string middle(string str){
    //checks the length of str
    int length = str.length();
    string middle_letter;
    // if length%2 gives no remainer, it knows it is even
    if (length%2 == 0){
        middle_letter = str.substr((length/2) -1,2); 
        //using .substr to extract the certain letters we need
        //since sam starts a 0 we subtract 1 to get the first character of the double and ,2 to get the letter next to it.
    }//phillip
    // it is odd
    else{
        middle_letter = str.substr((length-1)/2,1);
    }
    return middle_letter;
}