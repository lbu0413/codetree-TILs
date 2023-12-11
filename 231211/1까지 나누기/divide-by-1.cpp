#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int cnt = 0;
    int i = 1;
    while (true) {
        n /= i;
        cnt++;
        if (n <= 1) {
            cout << cnt;
            break;
        }
        i++;
    }
    return 0;
}