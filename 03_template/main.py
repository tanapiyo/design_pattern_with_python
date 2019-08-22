from char_display import CharDisplay
from string_display import StringDisplay

if __name__ == '__main__':
  char_display = CharDisplay("H")
  string_display = StringDisplay("Hello, World")
  string_display_japanese = StringDisplay("こんにちは")

  char_display.display()
  string_display.display()
  string_display_japanese.display()