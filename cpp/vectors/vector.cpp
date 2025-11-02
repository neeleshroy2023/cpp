#include <iostream>
#include <vector>

int main() {
    std::vector<int> numbers;
    int currentValue;
    
    std::cout << "Enter numbers (press Ctrl+D or non-number to stop):" << std::endl;
    
    while(std::cin >> currentValue) {
        numbers.push_back(currentValue);
    }
    
    std::cout << "You entered: ";
    
    for (int i=0; i < numbers.size(); i++) {
        std::cout << numbers[i] << " ";
    }
    
    std::cout << std::endl;
    
    return 0;
}