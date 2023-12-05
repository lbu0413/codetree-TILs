#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;

    double c = a + b;
    double d = a - b;

    cout << fixed;
    cout.precision(2);

    cout << c / d;
    return 0;
}