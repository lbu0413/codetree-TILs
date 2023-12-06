#include <iostream>
using namespace std;

int main() {
    int budget;
    cin >> budget;

    if (budget >= 3000) {
        cout << "book";
    }
    else if(budget >= 1000) {
        cout << "mask";
    }
    else {
        cout << "no";
    }
    return 0;
}