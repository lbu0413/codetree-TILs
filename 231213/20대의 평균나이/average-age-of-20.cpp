#include <iostream>
using namespace std;

int main() {
    int sum = 0;
    int cnt = 0;
    while (true) {
        int age;
        cin >> age;
        cout << fixed;
        cout.precision(2);
        if (age / 10 != 2) {
            cout << (double)sum / cnt;
            break;
        }
        sum += age;
        cnt++;
    }
    return 0;
}