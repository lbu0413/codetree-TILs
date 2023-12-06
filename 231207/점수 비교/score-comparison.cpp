#include <iostream>
using namespace std;
int main() {
    int math_a, eng_a;
    int math_b, eng_b;

    cin >> math_a >> eng_a;
    cin >> math_b >> eng_b;

    cout << (math_a > math_b && eng_a > eng_b);

    return 0;
}