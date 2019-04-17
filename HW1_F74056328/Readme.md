# Programming language HW1 common LISP

## Installation

- My environment: Windows 10

- Installed SBCL form [here](https://github.com/akovalenko/sbcl-win32-threads/wiki) using MSI package for 64-bit Windows

- Excute SBCL with Windows Powershell, using `sbcl --script .\<filename>.lsp`

* Note that `End Of File(EOF)` in Windows can be send by `ctrl+z` instead of `ctrl+d` in Linux.
    
    * Also, for each EOF signal, you have to press `enter` in Windows due to "blocking IO method"

----
## HW Problems

For each problem, the `.lsp` file(script) is provided.

I just use `(print <function>)` to show the result on terminal. Feel free to modify the parameter to check the result.

### Problem 1.1
- filename: prime.lsp
    - method: using recursion to checking every number that smaller than the number input.
    - if the number can be divide only by itself and 1, it\'s a prime number.

### Problem 1.2
- filename: palindrome.lsp
    - method: compare the input content with reversed itself, if all equal, it\'s palindrome.

### Problem 1.3
- filename: fib.lsp (using `(trace <function>)` to trace how function works)
    -  original recursion: Just original recursion call.
    
    -  tail recursion: Add two more arguments, `a` and `b` meaning the zeroth and the first number in the fibonacci series. <br> when using the function I write, remember to give `a b` => `0 1` respectively.

    - the tail recursion method is quite similar to iteration method, the number we want is computed through the recursion call

### Problem 2