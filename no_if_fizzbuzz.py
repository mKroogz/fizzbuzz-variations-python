def threes(valid):
    while(valid):
        return "Fizz"
    return ""
        
def fives(valid):
    while(valid):
        return "Buzz"
    return ""

def output_check(output, num):
    while(output):
        return output
    return num

for i in range(1, 101):
    output = ""
    output += threes(i % 3 == 0)
    output += fives(i % 5 == 0)
    output = output_check(output, i)
    print(output)