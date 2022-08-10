//Author: Josiel Perez
//Course: CSCI-135
//Instructor: Tong Yi
//Assignment: E7.1
//
//
//
//
#include <iostream>
using namespace std;

void sort2(double* p, double* q){
    double x = *p;
    
    if (p > q){
        *p = *q;
        *q = x;
    }
}
