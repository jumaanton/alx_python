def fibonacci_sequence(n):
    """ Returns a list containing the Fibonacci sequence up to n """
    if n < 1:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    fibonacci_list = [0, 1]
    for i in range(2, n):
        fibonacci_list.append(fibonacci_list[i - 1] + fibonacci_list[i - 2])
    return fibonacci_list
