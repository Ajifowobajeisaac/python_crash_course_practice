"""Control flow operations 'for', 'if' and 'elif'"""

# Append the right prefix ("nd" or "st") to numbers
print("Append the right prefix ('nd' or 'st') to numbers")
ordinals = [ordinal for ordinal in range(1, 10)]
print() 
[print(ordinal) for ordinal in ordinals]


print()
suffix = ''
for ordinal in ordinals:
    if ordinal == 1:
        suffix = 'st'
    elif ordinal == 2:
        suffix = 'nd'
    elif ordinal == 3:
        suffix = 'rd'
    elif ordinal > 3:
        suffix = 'th'
    print(f'{ordinal}{suffix}')


