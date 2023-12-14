#include <iostream>
using namespace std;

int main() {
    bool satisfied = true;

    for (int i = 0; i < 5; i++) {
        int num;
        cin >> num;

        if (num % 3 != 0) {
            satisfied = false;
        }
    }

    cout << (satisfied ? 1 : 0);
    return 0;
}