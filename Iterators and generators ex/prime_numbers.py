def get_primes(numbers):
    for number in numbers:
        if number <= 1:
            continue

        for divisor in range(2, number):
            if number % divisor == 0:
                break
        else:
            yield number
