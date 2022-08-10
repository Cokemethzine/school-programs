#include <iostream>
#include <fstream>
#include <cstdlib>
#include <climits>

using namespace std;

int main(){
    ifstream fin("Current_Reservoir_Levels.tsv");
    if (fin.fail()) {
        cerr << "File cannot be opened for reading." << endl;
        exit(1); // exit if failed to open the file
    }

    string junk;        // new string variable
    getline(fin, junk); // read one line from the file 

    string date;
    double eastSt, eastEl, westSt, westEl;
    double min = INT_MAX; // INT_MAX is the maximum value 'int' type can hold
                          // INT_MAX belongs to <climits> header.
                          // In C++, INT_MAX usually represent a very big number or infinity
    double max = INT_MIN;


    while (fin >> date >> eastSt >> eastEl >> westSt >> westEl) { 
        // this loop reads the file line-by-line
        // extracting 5 values on each iteration 
        
        fin.ignore(INT_MAX, '\n'); //skips to the end of line, 
                            //ignorring the remaining columns 

        // YOUR code
        if (eastSt < min){ // found a new candidate for 'min' value.
            min = eastSt;
        }
        if (eastSt > max){
            max = eastSt;
        }
    }
    cout << "minimum storage in East basin:" << min << " billion gallons" << endl;
    cout << "MAXimum storage in East basin:" << max << " billion gallons" << endl;

    fin.close();
}