#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;

    cout << n * n << endl;
    if (n < 5) {
        cout << "tiny";
    }
    return 0;
}