try:
    # Python 2
    xrange
except NameError:
    # Python 3, xrange is now named range
    xrange = range

for i in xrange(1, 101):
    print(i if i % 5 else "Buzz") if i % 3 else (
        "Fizz" if i % 5 else "FizzBuzz")
