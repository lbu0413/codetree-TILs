#include <iostream>
using namespace std;

int main() {
int cnt = 0;
    while (true) {
        int num;
        cin >> num;

        if (num % 2 == 1) {
            continue;
        }

        else if (num % 2 == 0) {
            cout << num / 2 << endl;
            cnt++;
        }
        if (cnt == 3) {
            break;
        }
        
    }
    return 0;
}