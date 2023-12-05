#include <iostream>
using namespace std;
int main() {
    
    int y, m, d;
    char c = '.';

    cin >> m;
    cin.get();
    cin >> d;
    cin.get();
    cin >> y;
    cout << y << c << m << c << d;
    return 0;
}