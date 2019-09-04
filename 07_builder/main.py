#長さが1以外usage
#plainでtextbuilder
#htmlでhtml-dire-construct-result-print


import sys
from application import TextBuilder, HTMLBuilder
from framework import Director

@classmethod
def __usage():
  print("Usage: if you want to make plain text, python main.py plain")
  print("Usage: if you want to make html, python main.py html")

def main():
  if len(sys.argv) != 2:
    __usage()
    sys.exit()

  if sys.argv[1] == "plain":
    text_builder = TextBuilder()
    director = Director(text_builder)
    director.construct()
    print(text_builder.get_result())
  elif sys.argv[1] == "html":
    html_builder = HTMLBuilder()
    director = Director(html_builder)
    director.construct()
    print("%sが作成されました。" % html_builder.get_result())
  else:
    __usage()
    sys.exit()

if __name__ == "__main__":
  main()