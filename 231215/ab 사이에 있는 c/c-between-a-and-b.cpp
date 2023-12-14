#include <iostream>
using namespace std;


int main() {
    int a, b, c;
    cin >> a >> b >> c;
    bool checker = false;
    for (int i = a; i <= b; i++) {
        if (i % c == 0) {
            checker = true;
        }

        if (checker) {
            break;
        }
    }
    cout << (checker ? "YES" : "NO");
    return 0;
}