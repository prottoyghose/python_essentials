#
# Example file for parsing and processing HTML
#

from html.parser import HTMLParser

metacount=0;
class MyHTMLParser(HTMLParser):
  def handle_comment(self,data):
    print("Encountered comment: ", data)
    pos = self.getpos()
    print ("\At line: ", pos[0], " positions: ", pos[1])

  def handle_starttag(self,tag,attrs):
    global metacount
    if tag == 'meta':
      metacount+=1

    print("Encountered tag: ", tag)
    pos = self.getpos()
    print ("At line: ", pos[0], " positions: ", pos[1])

  
  def handle_endtag(self, tag):
    print("Encountered tag: ", tag)
    pos = self.getpos()
    print ("At line: ", pos[0], " positions: ", pos[1])

  def handle_data(self, data):
    print("Encountered data: ", data)
    pos = self.getpos()
    print ("At line: ", pos[0], " positions: ", pos[1])


def main():
  parser = MyHTMLParser()
  f = open("samplehtml.html")
  if f.mode == 'r':
    contents = f.read()
    parser.feed(contents)

if __name__ == "__main__":
  main();
  
