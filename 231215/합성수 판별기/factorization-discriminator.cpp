#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    bool prime = false;
    for (int i = 2; i < n; i++) {
        if (n % i == 0) {
            prime = true;
        }
    }

    cout << (prime ? 'C' : 'N');

    return 0;
}