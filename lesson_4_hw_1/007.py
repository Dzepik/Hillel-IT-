

def convert(string: str):
  num = 0
  for i in string:
    num += (ord(i) - 48)
  print(num)


if __name__ == '__main__':
  user_input = input("Enter the numbers: ")
  convert(user_input)