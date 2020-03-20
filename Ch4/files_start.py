#
# Read and write files using the built-in Python file methods
#

def main():  
  # Open a file for writing and create it if it doesn't exist
  f = open("demo.txt","w+")

  # Open the file for appending text to the end
  #f = open("textfile.txt","a")

  #Read an existing file and put out the contents
  #f = open("textfile.txt","r")

  # write some lines of data to the file
  for i in range (10):
     f.write("This is line " + str(i) + "\r\n")
  
  # close the file when done
  f.close()
  
  # Open the file back up and read the contents
  # if f.mode == 'r':
  #   #f.read() reads the whole thing at once in memory. Bad practice for memory exhaustive app
  #   #Use f.readLine() method in order to read line by line in python
  #   contents = f.read()
  #   print(contents)

    
if __name__ == "__main__":
  main()
