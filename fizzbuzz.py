def fizzbuzz(number):
    for i in range(1, number+1):
        string = ''
        if i % 3 == 0:
            string += 'fizz'
        if i % 5 == 0:
            string += 'buzz'
        print(string or i)


if __name__ == '__main__':
    user_input = int(input('Please enter a positive number:\n'))
    fizzbuzz(user_input)
