#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.

    int a = 5, b = 6, c = 7;
    int tmp, tmp2;

    tmp = b;
    tmp2 = c;

    b = a;
    c = tmp;
    a = tmp2;


    cout << a << endl;
    cout << b << endl;
    cout << c;

    return 0;
}