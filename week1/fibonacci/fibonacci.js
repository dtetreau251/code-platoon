/*given a num returns the n-th 
Fibonacci number*/
const fib = (n) => n < 2 ? n : fib(n-1) + fib(n-2);

module.exports = {fib}