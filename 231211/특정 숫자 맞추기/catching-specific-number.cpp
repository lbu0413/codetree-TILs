#include <iostream>
using namespace std;

int main() {
    
    while (true) {
        int num;
        cin >> num;

        if (num < 25) {
            cout << "Higher" << endl;
        }
        else if (num > 25) {
            cout << "Lower" << endl;
        }
        else {
            cout << "Good";
            break;
        }
    }
    return 0;
}