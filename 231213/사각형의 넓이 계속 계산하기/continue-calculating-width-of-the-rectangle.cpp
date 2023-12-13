#include <iostream>
using namespace std;

int main() {
    
    while (true) {
        int width, height;
        char letter;
        
        cin >> width >> height >> letter;
        
        cout << width * height << endl;
        if (letter == 'C') {
            break;
        }
        else {
            continue;
        }
    }
    return 0;
}