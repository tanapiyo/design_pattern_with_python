from idcard import IdCardFactory

def main():
  factory = IdCardFactory()
  card1 = factory.create("結城浩")
  card2 = factory.create("とむら")
  card3 = factory.create("佐藤花子")

  card1.use()
  card2.use()
  card3.use()

if __name__ == '__main__':
  main()