#include <iostream>
using namespace std;

int main() {
    int A_math, A_english;
    int B_math, B_english;

    cin >> A_math >> A_english >> B_math >> B_english;

    if (A_math > B_math) {
        cout << "A";
    }
    else if (B_math > A_math) {
        cout << "B";
    }
    else {
        if (A_english > B_english) {
            cout << "A";
        }
        else {
            cout << "B";
        }
    }
    return 0;
}