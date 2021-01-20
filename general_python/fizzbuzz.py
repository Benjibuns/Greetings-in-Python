def fizz_buzz(first, last):
    for num in range(first, last + 1):
        if num % 3 == 0 and num % 5 == 0:
            num = "FizzBuzz"
        elif num % 3 == 0:
            num = "Buzz"
        elif num % 5 == 0:
            num = "Fizz"

        print(num)


fizz_buzz(1, 100)
