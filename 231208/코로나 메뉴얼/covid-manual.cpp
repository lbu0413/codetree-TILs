#include <iostream>
using namespace std;

int main() {
    
    char s1, s2, s3;
    int t1, t2, t3;
    int A, B, C, D;

    cin >> s1 >> t1;
    cin >> s2 >> t2;
    cin >> s3 >> t3;

    if (s1 == 'Y' && t1 >= 37) {
        A += 1;
    }
    else if (s1 == 'N' && t1 >= 37) {
        B += 1;
    }
    else if (s1 == 'Y' && t1 < 37) {
        C += 1;
    }
    else {
        D += 1;
    }

    if (s2 == 'Y' && t2 >= 37) {
        A += 1;
    }
    else if (s2 == 'N' && t2 >= 37) {
        B += 1;
    }
    else if (s2 == 'Y' && t2 < 37) {
        C += 1;
    }
    else {
        D += 1;
    }

    if (s3 == 'Y' && t3 >= 37) {
        A += 1;
    }
    else if (s3 == 'N' && t3 >= 37) {
        B += 1;
    }
    else if (s3 == 'Y' && t3 < 37) {
        C += 1;
    }
    else {
        D += 1;
    }


    if (A >= 2) {
        cout << 'E';
    }
    else {
        cout << 'N';
    }

    return 0;
}