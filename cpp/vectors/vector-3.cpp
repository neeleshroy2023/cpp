#include <iostream>
#include <vector>

int main() {
    std::vector<int> numbers{10, 20, 30};

    for (int& num : numbers) {
        num *= 2;
    }

    std::cout << "After: ";
    for (int num : numbers) {
        std::cout << num << " ";
    }

    std::cout << std::endl;

    return 0;
}