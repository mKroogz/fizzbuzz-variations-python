def fizz_buzzer(num):
    if (num < 101):
        output = ""
        if (num % 3 == 0):
            output += "Fizz"
        if (num % 5 == 0):
            output += "Buzz"
        if (output == ""):
            output = num
        print(output)
        fizz_buzzer(num + 1)

fizz_buzzer(1)