def fib(n):
   if n <= 1:
       return n
   else:
       return(fib(n-1) + fib(n-2))

x = int(input("Entet No. of Terms: "))

if x <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(x):
       print(fib(i))
