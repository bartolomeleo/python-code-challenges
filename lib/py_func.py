def dicUnpack(a,b,c):
    print(a,b,c)

args={'a':1,'b':2, 'c': 3}

dicUnpack(**args)

def make_incrementor(n):
    return lambda x: x + n

f=make_incrementor(42)

g=make_incrementor(42)(0)

print(f(0), g)

pairs = [(2,'two', 'fs'), (1,'one', 'e'), (4,'four','f'), (3,'three','ds')]

# Define the key function
def get_pair_value(pair, choice):
    return pair[choice]

# Sort the pairs by the second value (the letters)
sortLetter = pairs.copy()
sortLetter.sort(key=lambda pair: get_pair_value(pair, 1))

# Sort the pairs by the first value (the numbers)
sortNumber = pairs.copy()
sortNumber.sort()

print(sortLetter)  # Output: [(1, 'one'), (4, 'four'), (3, 'three'), (2, 'two')]
print(sortNumber)  # Output: [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
