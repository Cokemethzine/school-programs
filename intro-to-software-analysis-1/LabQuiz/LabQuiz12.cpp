//
//
//
//
//
//
//
#include <iostream>
using namespace std;

class Money{
    public:
        int dollars;
        int cents;
};

Money add_money(Money x, Money y){
    int cents_making_dollars = (x.cents + y.cents)/100; // gives the dollars amount of cent over 100
    int rest_of_cents = (y.cents + x.cents)%100; // gets left over cents
    Money total = {x.dollars + y.dollars + cents_making_dollars, rest_of_cents};
    return total;


}