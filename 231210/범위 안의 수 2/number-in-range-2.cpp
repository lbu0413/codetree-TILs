#include <iostream>
using namespace std;

int main() {
    int sum = 0, cnt = 0;
    double avg;
    for (int i = 0; i < 10; i++) {
        int num;
        cin >> num;

        if (0 <= num && num <= 200) {
            sum += num;
            cnt++;
        }
    }

    cout << fixed;
    cout.precision(1);

    avg = (double)sum / cnt;

    cout << sum << " " << avg;
    return 0;
}