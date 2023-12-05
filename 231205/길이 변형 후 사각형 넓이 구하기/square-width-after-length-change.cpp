#include <iostream>
using namespace std;
int main() {
    int width, height, area;
    cin >> width >> height;
    
    width += 8;
    height *= 3;
    area = width * height;

    cout << width << endl;
    cout << height << endl;
    cout << area;
    return 0;
}