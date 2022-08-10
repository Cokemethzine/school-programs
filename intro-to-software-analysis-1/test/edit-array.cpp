/*
Josiel Perez
CSCI-136
Minh Nguyen
Using arrays to store, update, and retrieve numbers
*/

#include <iostream>
using namespace std;

int main(){
// declared my variables
    int array[10], inputIndex, inputValue , i; //

    for(i = 0; i < 10; i++)     
        array[i] = 1;
    
    bool isRunning = true; //

    for(i = 0; i < 10; i++) 
        std::cout << array[i] << " "; //
// checked to is if its true then will run
    while(isRunning){
        std::cout << endl;

        std::cout << "Input index: " << std::endl;
        std::cin >> inputIndex;
        std::cout << "Input value: " << std::endl;
        std::cin >> inputValue;

        if(inputIndex < 10 && inputIndex >= 0){
            array[inputIndex] = inputValue;
            for(int i = 0; i < 10; i++) 
                std::cout << array[i] << " ";
        } else{
            std::cout << "Index out of range. Exit." << std::endl;
            isRunning = !isRunning;
        }
    }
    return 0;
}