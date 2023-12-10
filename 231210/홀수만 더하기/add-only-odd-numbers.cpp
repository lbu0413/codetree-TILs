#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int sum_val = 0;

    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;

        if (num % 2 == 1 && num % 3 == 0) {
            sum_val += num;
        }
        
    }
    cout << sum_val;
    return 0;
}