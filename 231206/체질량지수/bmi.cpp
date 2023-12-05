#include <iostream>
using namespace std;
int main() {
    int height, weight;
    cin >> height >> weight;

    int height_to_m = height / 100;
    int bmi = (weight * 100 * 100) / (height * height);

    cout << bmi << endl;
    if (bmi >= 25) {
        cout << "Obesity";
    }

    return 0;
}