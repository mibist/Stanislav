numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

def odd_numbers(number):
    return number % 2 != 0
def square(number):
    return number ** 2

result = list(map(square, filter(odd_numbers, numbers)))
print(result)