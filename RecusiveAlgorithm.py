# Recursive is Latin (recusio) meaning to run back
#  here is A factorial example for recursion

def iterative_factorial(n):  # iterative FASTer than recursion
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact


print(iterative_factorial(5))


def recur_factorial(n):
    if n == 1:
        return n
    else:
        temp = recur_factorial(n - 1)
        temp *= n
        return temp


print(recur_factorial(5))


# Permutations: ABC, BAC, CA, etc
# String are immutable

def permute(string, pocket=''):
    if len(string) == 0:
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[:i]
            back = string[i + 1:]
            together = front + back
            permute(together, letter + pocket)


print(permute('AB', ''))

