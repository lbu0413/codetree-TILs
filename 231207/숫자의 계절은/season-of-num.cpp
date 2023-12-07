#include <iostream>
using namespace std;

int main() {
    int month;
    cin >> month;

    if (month >= 3 && month <= 5) {
        cout << "Spring";
    }
    else if (month >= 6 && month <= 8) {
        cout << "Summer";
    }
    else if (month >= 9 && month <= 11) {
        cout << "Fall";
    }
    else {
        cout << "Winter";
    }
    return 0;
}