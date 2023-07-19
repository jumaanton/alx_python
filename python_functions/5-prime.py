def is_prime(number):
    """Returns True if number is prime, False otherwise"""
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False

    return True 