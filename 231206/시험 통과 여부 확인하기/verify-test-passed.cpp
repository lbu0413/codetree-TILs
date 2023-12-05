#include <iostream>
using namespace std;

int main() {
    int score;
    cin >> score;

    if (score >= 80) {
        cout << "pass";
    } 
    else {
        int need_more = 80 - score;
        cout << need_more << " more score";
    }
    return 0;
}