#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int a = 3, b = 5;
    int tmp = a;
    a = b;
    b = tmp;

    cout << a << endl;
    cout << b;
    return 0;
}