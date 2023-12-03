#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    int a = 2, b = 5;
    int tmp = a;
    a = b;
    b = tmp;

    std::cout << a << std::endl;
    std::cout << b;
    return 0;
}