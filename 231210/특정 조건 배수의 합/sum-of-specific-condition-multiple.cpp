#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    int sum = 0;

    int big, small;
    
    if (a >= b) {
        big = a;
        small = b;
    } 
    else {
        big = b;
        small = a;
    }

    for (int i = small; i <= big; i++){
        if (i % 5 == 0) {
            sum += i;
        }
    }
    cout << sum;
    return 0;
}