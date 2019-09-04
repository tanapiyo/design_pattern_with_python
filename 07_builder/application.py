from framework import Builder
import os

class TextBuilder(Builder):
  def __init__(self):
    self.__buffer = []
  
  def make_title(self, title: str) -> None:
    self.__buffer.append("======================")
    self.__buffer.append("『%s』" % title)
    self.__buffer.append("")
  
  def make_string(self, string: str) -> None:
    self.__buffer.append("■%s" % string)

  def make_items(self, items: list) -> None:
    for item in items:
      self.__buffer.append(" ・%s" % item)
    self.__buffer.append("")
  
  def close(self) -> None:
    self.__buffer.append("======================")
  
  def get_result(self) -> str:
    return '\n'.join(self.__buffer)

class HTMLBuilder(Builder):
  def __init__(self):
    self.__filename = ""
    self.__writer = ""#file openしたときの型で初期化
    
  
  def make_title(self, title: str) -> None:
    self.__filename = title + ".html"
    try:
      self.__writer = open(self.__filename, mode="w")
    except IOError as e:
      print(e)
    self.__writer.write("<!DOCTYPE html><html><head><meta http-equiv='Content-Type' content='text/html; charset=UTF-8' /><title>%s</title></head><body>" % title)
    self.__writer.write("<h1>%s<h1>" % title)
      
  def make_string(self, string: str) -> None:
    self.__writer.write("<h1>%s<h1>" % string)

  def make_items(self, items: list) -> None:
    self.__writer.write("<ul>")
    for item in items:
      self.__writer.write("<li>%s</li>" % item)
    self.__writer.write("</ul>")
  
  def close(self) -> None:
    self.__writer.write("</body></html>")
    self.__writer.close()
  
  def get_result(self) -> str:
    return self.__filename