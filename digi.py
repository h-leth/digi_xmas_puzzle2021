ascii_list = [115, 52, 52, 48, 58, 47, 47, 52, 115, 112,
              109, 116, 114, 51, 112, 110, 50, 112, 52, 46, 121, 122]
solution = ''

for i in ascii_list:
    if chr(i).isalpha():
        solution += chr(i - 11)
    if chr(i).isdigit():
        solution += chr(i + 64)
    if not chr(i).isalpha() and not chr(i).isdigit():
        solution += chr(i)

print(solution)
