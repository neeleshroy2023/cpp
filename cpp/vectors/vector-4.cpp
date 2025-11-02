#include <iostream>
#include <vector>
#include <string>

int main() {
    std::vector<std::string>fruits {"apple", "orange", "pears"};

    for (const std::string& fruit : fruits) {
        std::cout << fruit << " ";
    }

    return 0;
}