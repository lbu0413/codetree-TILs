#include <iostream>
using namespace std;

int main() {
    int n, m;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> m;
        if (m % 2 != 0 && m % 3 == 0) {
            cout << m << endl;
        }

    }
    return 0;
}