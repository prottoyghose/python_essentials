#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta, datetime
import time


def main():
  # Print the name of the OS
  print (os.name)

  # Check for item existence and type
  print("Item exists: " + str (path.exists("textfile.txt")))
  print("Item is a file: " + str (path.isfile("textfile.txt")))
  print("Item exists: " + str (path.isdir("textfile.txt")))
  
  # Work with file paths
  print("Item path: " + str(path.realpath("textfile.txt")))
  print("Item path and name: " + str(path.split(path.realpath("textfile.txt"))))

  # Get the modification time
  t = time.ctime(path.getmtime("textfile.txt"))
  print(t)

  #Calculate How long ago the file was modified
  td = datetime.now() - datetime.fromtimestamp(path.getmtime("textfile.txt"))
  print(td)


if __name__ == "__main__":
  main()
