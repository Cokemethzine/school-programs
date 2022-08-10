#include <iostream>
using namespace std;

int main()
{
    // state the variables
    int x, y;
    double z;
    // Asking user input
    cout << "Enter the number of gallons of gas in the tank:" << endl;
    cin >> x;
    cout << "Enter the fuel efficiency in miles per gallon:" << endl;
    cin >> y;
    cout << "Enter the price of gas per gallon:" << endl;
    cin >> z;
    // printing the cost per 100 miles
    double a = 100 *(z/y);
    
    
    // how far the car can go with the gas in the tank
    int c = x * y;
    // print statement
    cout << "The cost per 100 miles is " << a << " and the car can go " << c << " miles with the gas in the tank";

    return 0;
    
}