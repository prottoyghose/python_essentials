#
# Example file for working with classes
#


class myClass():

  def method1(self):
    print("myClass method1")
  
  def method2(self,someString):
    print("myclass method2 "+ someString)

class anotherClass(myClass):

  def method1(self):
    myClass.method1(self)
    print("anotherClass method1")
  
  def method2(self,someString):
    print("anotherClass method2 ")

def main():
  # c = myClass()
  # c.method1()
  # c.method2("Prottoy")

  c2 = anotherClass()
  c2.method1()
if __name__ == "__main__":
  main()
