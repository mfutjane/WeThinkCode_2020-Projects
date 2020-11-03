import random

code_range = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
code = []
for i in range(4):
    digit_index = random.randint(1, len(code_range) - 1)
    digit = code_range[digit_index]
    code.append(digit)
print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')
print("".join(code))