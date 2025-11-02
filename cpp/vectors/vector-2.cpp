#include <iostream>
#include <vector>

int main() {
    std::vector<int> numbers;
    numbers.push_back(10);
    numbers.push_back(20);
    numbers.push_back(30);

    if(!numbers.empty()) {
        std::cout << "Last element: " << numbers.back() << std::endl;
    }

    std::cout << "All numbers: ";
    for (int num : numbers) {
        std::cout << num << " ";
    }

    std::vector<int> scores(5, -1);
    std::cout << "Initialized scores: ";
    for (int score : scores) {
        std::cout << score << " ";
    }
    std::cout << std::endl;
}