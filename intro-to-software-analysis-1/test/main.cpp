#include <iostream>;
using namespace std;


int main()
{
    cout << "Enter name in format of first name first, last name last: ";
    string name;
    cin >> name;

    size_t index = name.find(" ");

    if (index != string::npos)
    {
        cerr << " no space in input name, cannot enter" << endl;
        return -1;
    }

    string firstName = name.substr(0,index);
    string lastName = name.substr(index -1);
    cout << lastName + ", " + firstName << endl;

    return 0;

}