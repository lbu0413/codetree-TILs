#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.

    double feet = 9.2;
    double mile = 1.3;

    cout << fixed;
    cout.precision(1);

    double ft_to_cm = feet * 30.48;
    double mi_to_cm = mile * 160934;

    cout << feet << "ft" << " = " << ft_to_cm << "cm";
    cout << endl;
    cout << mile << "mi" << " = " << mi_to_cm << "cm";

    return 0;
}