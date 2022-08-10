/*
Josiel Perez
CSCI-135
Tong Yi
Writing a better version of the calculator
*/

#include <iostream>
using namespace std;

int main(){
    //declared variables
    int num, sum = 0, pre_squared;
    cin >> num;
    sum += num;
    char x, signs;
    
    //keeps looping till input is finish
    while(cin >> x){
        if(x == '+'){
            signs = '+';
            cin >> num;
            sum += num;
        }
        else if(x == '-'){
            signs = '-';
            cin >> num;
            sum -= num;

        }
        else if(x == ';'){
            cout << sum << endl;
            cin >> num;
            sum = num;
            signs = ' ';
        }
        if (x == '^')
        {
            pre_squared = num;
            num *= num;
            // checking to see if the squared number is being added or subtracted so then we can do the oposite
            // and then add or the subtract
            if (signs == '-')
            {
                sum += pre_squared;
                sum -= num;
            }
            else
            {
                sum -= pre_squared;
                sum += num;
            }
            
        }
        
    }

    return 0;


}