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

    string date, earlier, later;
    double eastSt, eastEl, westSt, westEl;

    cout << "Please enter the earlier date: ";
    cin >> earlier;
    cout << "Please enter the later date: ";
    cin >> later;

    string dates_arr[400];
    double westEl_arr[400];

    int index = 0;
    while (fin >> date >> eastSt >> eastEl >> westSt >> westEl){ 
        // this loop reads the file line-by-line
        // extracting 5 values on each iteration 
        
        fin.ignore(INT_MAX, '\n'); //skips to the end of line, 
                            //ignorring the remaining columns 

        // YOUR code
        // In C++, you can compare string for inequality.
        if (earlier <= date and date <= later){
            dates_arr[index] = date;
            westEl_arr[index] = westEl;
            index++;
        }

        if(date > later){ //amke your code more efficient.
            break;
        }
    }
    for ( int i = index-1; i >= 0; i--){
        cout << dates_arr[i] << " " << westEl_arr[i] << endl;
    }

    fin.close();
}