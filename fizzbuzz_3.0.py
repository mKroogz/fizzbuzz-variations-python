def fizz_buzzer(num):
    both = (num % 3 == 0 and num % 5 == 0) and "FizzBuzz"
    three = num % 3 == 0 and "Fizz"
    five = num % 5 == 0 and "Buzz"
    print(both or three or five or num)
    done = (num > 99) or fizz_buzzer(num + 1)

fizz_buzzer(1)