digits = [0,0,0,9]
result = ''.join(map(str, digits))
number = list(str(int(result)+1))
int_numbers = [int(num) for num in number]
print(int_numbers)