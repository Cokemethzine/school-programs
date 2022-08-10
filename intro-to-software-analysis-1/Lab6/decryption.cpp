//Author: Josiel Perez
//Course: CSCI-135
//Instructor: Minh Nguyen
//Assignment: Lab 6D
//
//
//
//
//
//
//
//
//
//Decryption

#include <iostream>
#include <cctype> // contains some useful function for char types
#include <string> // contains some useful function for string types

using namespace std;

string encryptVigenere(string plaintext, string keyword);
string encryptCaesar(string plaintext, int rshift);
char shiftChar(char c, int rshift);
string decryptCaesar(string ciphertext, int lshift);
string decryptVigenere(string ciphertext, string keyword);
int charindex(char o);




int main(){
    string a = "",b;
    int d;
    cout << "Enter Plaintext: ";
    getline(cin, a);
// caesar cipher
    cout << "= Caesar =" << endl;

    cout << "Enter shift: ";
    cin >> d;

    cout << "Ciphertext: " << encryptCaesar(a,d) << endl;
    cout << "Decrypted: " << decryptCaesar(encryptCaesar(a, d), d) << endl;

// vigenere cipher
    cout << "= Vigenere =" << endl;

    cout << "Enter keyword: ";
    cin >> b;

    cout << "Ciphertext:" << encryptVigenere(a,b) << endl;
    cout << "Decrypted: " << decryptVigenere(encryptVigenere(a,b),b) << endl;
}

string decryptCaesar(string ciphertext, int lshift){
    string plaintext = "";
    int index = -1;
	while (ciphertext[++index])
		plaintext += shiftChar(ciphertext[index], -lshift);
	return plaintext;
}


int charindex(char o){
    int ascii = (int)o-(isupper(o)?(int)'A':(int)'a');
    return ascii%26;
}

string decryptVigenere(string plainText, string keyword){
    string r = "";
    int i = -1;
    int index = -1;
    while(plainText[++i]){
        if(!isalpha(plainText[i]))
            r += plainText[i];
        else
            r +=shiftChar(plainText[i], -charindex(keyword[++index%keyword.length()]));
    }
    return r;
}

string encryptCaesar(string plaintext, int rshift){
    //apply shift char function to all characters in one string
    //iterate thru the plaintext, shift charcter by character, and applied it
    // to another string
    string ans;
    for(int i=0;i<plaintext.size();i++)
        ans += shiftChar(plaintext[i], rshift);
    return ans;

}

string encryptVigenere(string plaintext, string keyword){
    string ans;
    int j =0;
    for (int i = 0; i < plaintext.size(); i++){
        ans += shiftChar(plaintext[i], keyword[j] -'a');
        if (isalpha(plaintext[i])) j++;

        if (j == keyword.size()) j =0;
    }
    return ans;
}

char shiftChar(char c, int rshift){
    // We are wokring with the alphabet, so we need to find a way to convert
    // ACII order to 0-indexed alphabetical oder (0-25)
    // 'a'
    /*(if(islower(c))
        return(c-'a' +rshift)%26 + 'a';
        // %26 is to deal with the wrap around =, 26 is no. of letter
    if(isupper(c))
        return(c-'A'+rshift)%26 +'A';
    
    return c;*/
    if(!isalpha(c) || rshift==0)
        return c;
    int index;
    if (rshift > 0)
    {
        int a = isupper(c)? (int)'A':(int)'a';
        index = (((int)c + rshift-a)%26)+a;
    }
    else
    {
        int z = isupper(c)?(int)'Z':(int)'z';
        index = (((int)c + rshift-z)%26)+z;
    }
    return (char)index;
}