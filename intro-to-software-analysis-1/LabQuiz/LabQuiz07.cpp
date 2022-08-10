#include <iostream>
#include <algorithm>
using namespace std;



/*int max3(int a, int b, int c)   
{ 
    if ( a > b && a > c )
        return a;
    else if ( b > a && b > c )
        return b;
    else if ( c > a && c > b )
        return c;
}

int main(){
    cout << max3(2,4,1);

}*/



int max3(int a, int b, int c){
    int hold,max_result;
    hold = max(a,b);
    max_result = max(hold,c);
    return max_result;

}

int main(){
    cout << max3(2,4,1);

}