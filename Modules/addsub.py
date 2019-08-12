def add(a, b):
  print(a+b)

def subtract(a, b):
  print(abs(a-b))

if __name__ == "__main__":
    import sys
    add(int(sys.argv[1]), int(sys.argv[2]))