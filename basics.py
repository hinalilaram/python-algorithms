import math


#Implement Factorial

#Sequential Implementation
def factorial_sequential(n):
    if n < 0:
        return "You have Entered a negative number"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(factorial_sequential(5))


#Recursiev Implementation
def factorial_recursive(n):
    if n < 0:
        return "You have Entered a negative number"
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


print(factorial_recursive(5))

# - Implement *** prints
#       -- Upper Triangle & its reverse
#       -- Lower Triangle & its reverse
#       -- Diamond (horizontal & vertical)
def upper_triangle_right(n):
    for i in range(n + 1):
        for j in range(0, i):
            print('* ', end='')
        print()


def upper_triangle_left(n):
    for i in range(n):
        print('  ' * ((n - 1) - i) + ' *' * (1 + i))


def lower_triangle_right(n):
    for i in range(n):
        print(" " * (2 * i) + "* " * (n - i))


def lower_triangle_left(n):
    for i in range(n):
        print("* " * (n - i))


def vertical_diamond():
    for i in range(5):
        print(' ' * (5 - i) + '* ' * (1 * i))
    for i in range(6):
        print(' ' * (i * 1) + '* ' * (5 - i))


def horizontal_diamond():
    for i in range(5):
        print('    ' * (5 - i) + '   *    ' * (1 * i))
    for i in range(6):
        print('    ' * (i * 1) + '   *    ' * (5 - i))


print('Upper Triangle Right')
upper_triangle_right(5)
print('Upper Triangle Left')
upper_triangle_left(5)
print('Lower Triangle Right')
lower_triangle_right(5)
print('Lower Triangle Left')
lower_triangle_left(5)
print('Vertical Diamond')
vertical_diamond()
print('Horizontal Diamond')
horizontal_diamond()
# - Implement consecutive-number prints
#       -- Upper Triangle & its reverse
#       -- Lower Triangle & its reverse
#       -- Diamond (horizontal & vertical)
