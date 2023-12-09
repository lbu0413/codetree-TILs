#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int classroom = 0, aisle = 0, bathroom = 0;
    for (int i = 1; i <= n; i++) {

        if (i % 12 == 0) {
            bathroom++;
        }
        else if (i % 3 == 0) {
            aisle++;
        }
        else if (i % 2 == 0) {
            classroom++;
        }
        
    }

    cout << classroom << " " << aisle << " " << bathroom;
    return 0;
}