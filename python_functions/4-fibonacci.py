def fibonacci_sequence(n):
    """ Returns a list containing the Fibonacci sequence up to n """
    if n < 1:
        return None
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibonacci_list = [1, 1]
    for i in range(2, n):
        fibonacci_list.append(fibonacci_list[i - 1] + fibonacci_list[i - 2])
    return fibonacci_list
