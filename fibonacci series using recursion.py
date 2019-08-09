def caller():
    n=int(input("How many terms:- "))
    for i in range(0,n):
      print(fibonacci(i))
      i+=1

def fibonacci(i):
    if i<=1:
      return i
    else:
      return (fibonacci(i-1)+fibonacci(i-2))
    
