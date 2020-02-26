#include <iostream>
#include "number_theory.hpp"

int main()
{
    int total;
    std::cin >> total;

    for (int i = 0; i < total; ++i)
    {
        std::cout << i << " : " << nt::fib(i) % nt::mod << std::endl;
    }
}