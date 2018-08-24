#include <iostream>

void getMemoryChart();

int main() {
    getMemoryChart();
}

void getMemoryChart() {
    bool b;
    char ch;
    short si; int i; long l;

    std::cout << "MEMORY CHART" << std::endl;
    std::cout << "======== NOTE: 1 byte = 8 bits." << std::endl;
    std::cout << "bool: "   << sizeof(b) << " byte" << std::endl;
    std::cout << "char: "   << sizeof(ch) << " byte" << std::endl;
    std::cout << "short: "  << sizeof(si) << " bytes" << std::endl;
    std::cout << "int: "    << sizeof(i) << " bytes" << std::endl;
    std::cout << "long: "   << sizeof(l) << " bytes" << std::endl;
}