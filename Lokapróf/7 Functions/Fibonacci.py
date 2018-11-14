"""The Fibonacci sequence is : 1,1,2,3,5,8,13
Write a function, fibo, to print the first N numbers
of the Fibonacci sequence. There should be one space between the
elements. Also write a statement to call fibo."""

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

num = int(input("Input the length of Fibonacci sequence (n>=1): "))

if num >= 0:
    for x in range(1, num+1):
        print(fibo(x), end=" ")