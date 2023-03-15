#n! = 1 * 2 * 3 * ... * n
def fact(n):
      product = 1
      for i in range(n):
            product = product * (i+1)
      print(f"Factorial is: {product}")

if __name__ == "__main__":
      n = int(input("Enter a number: "))
      fact(n)