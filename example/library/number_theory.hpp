#pragma once

namespace nt
{
const int mod = 1000000007;

long long fib(int n)
{
    return n <= 1 ? n : fib(n - 1) + fib(n - 2);
}

long long factorial(int n)
{
    return n <= 1 ? 1 : n * factorial(n - 1);
}
} // namespace nt