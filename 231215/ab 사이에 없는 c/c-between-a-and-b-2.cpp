#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;

    bool nexist = true;

    for (int i = a; i <= b; i++) {
        if (i % c == 0) {
            nexist = false;
        }
    }
    cout << (nexist ? "YES" : "NO");
    return 0;
}