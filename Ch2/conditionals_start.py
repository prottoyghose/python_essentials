#
# Example file for working with conditional statements
#

def main():
  x, y = 1000, 1000

  # conditional flow uses if, elif, else  
  if (x<y):
    st = "X is less than Y"
  elif(x==y):
    st = "X is equal to Y"
  else:
    st = "X is greater than Y"
  
  print(st)

  # conditional statements let you use "a if C else b"
  

if __name__ == "__main__":
  main()
