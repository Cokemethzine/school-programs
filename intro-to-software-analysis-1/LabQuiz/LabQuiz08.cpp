#include <iostream>
using namespace std;

void remove_e(string & sentence){
    string word = "";
    for(int i = 0; i < sentence.length(); i++){
        if(sentence[i] != 'e')
            word = word + sentence[i];
    }
    sentence = word;
}

