for i in range(1, 101):
    both = (i % 3 == 0 and i % 5 == 0) and "FizzBuzz"
    three = i % 3 == 0 and "Fizz"
    five = i % 5 == 0 and "Buzz"
    print(both or three or five or i)
