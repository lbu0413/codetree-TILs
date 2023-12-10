#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    int sum = 0;
    double cnt = 0;
    double avg;

    for (int i = a; i <= b; i++) {
        if (i % 5 == 0 || i % 7 == 0) {
            sum += i;
            cnt++;
        }
    }
    avg = sum / cnt;
    cout << fixed;
    cout.precision(1);
    cout << sum << " " << avg;
    return 0;
}