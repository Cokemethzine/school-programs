/*
Josiel Perez
CSCI-135
Tong Yi
Making a function that swaps its three arguments to arrange them in sorted order.
*/

#include <iostream>
using namespace std;
void sort2(int& a, int& b);
void sort3(int& a, int& b, int& c);



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
void sort3(int& a, int& b, int& c)
{
    sort2(a, b);
    sort2(a, c);
    sort2(b, c);
}
