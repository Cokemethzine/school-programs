
/*
Josiel Perez
CSCI-135
Tong Yi
Making a function that swaps the values of a and b if a is greater than b and otherwise
leaves a and b unchanged
*/

#include <iostream>
using namespace std;
void sort2(int& a, int& b);

/*int main(){
    int c,d;
    cin >> c >> d;
    sort2(c,d);

    cout << c << endl << d;
    return 0;
}
*/

void sort2(int& a, int& b)
{
    
    if (a > b)
    {
        int temp_a;
        temp_a = a;
        a = b;
        b = temp_a;

    }
    else
    {
        a = a;
        b = b;
    }
    
}