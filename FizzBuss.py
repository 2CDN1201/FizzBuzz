def fizzbuzz(n):
  #1からnまでの数字を出力する。
  #3の倍数の場合は"Fizz"、5の倍数の場合は"Buzz"、
  #3と5の両方の倍数の場合は"FizzBuzz"を出力する。
  for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
      print("FizzBuzz")
    elif i % 3 == 0:
      print("Fizz")
    elif i % 5 == 0:
      print("Buzz")
    else:
      print(i)

# いくつまで数えるか
num = input("いくつまで数えますか？")
fizzbuzz(int(num))
