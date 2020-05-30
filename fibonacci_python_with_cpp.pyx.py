def fib(int n):
   return fib_c

cdef int fib_c(int n):
   if n <= 1:
       return n
   else:
       return(fib_c(n-1) + fib_c(n-2))

x = int(input("Entet No. of Terms: "))

if x <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(x):
       print(fib_c(i))
