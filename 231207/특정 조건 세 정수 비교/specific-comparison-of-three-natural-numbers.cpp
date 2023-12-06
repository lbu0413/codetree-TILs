#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    int min = 101;
    cin >> a >> b >> c;

    if (a <= b && a <= c) {
        min = a;
    }
    else if (b <= a && b <= c) {
        min = b;
    }
    else {
        min = c;
    }

    cout << (a == min) << " ";
    cout << (a == b && a == c);
    return 0;
}