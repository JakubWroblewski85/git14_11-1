# Program sprawdzający czy słowe jest palindromem (czytane od tyłu brzmi tak samo)
word = str(input("Wpisz słowo: "))
word = word.replace(" ", "")
word = word.lower()
reverse_word = (word[::-1])
print (reverse_word)
if reverse_word == word:
    print("To jest palindrom")
else:
    print(f'{word} nie jest palindromem')

# reverse = reversed(slowo)
# print(''.join(reverse))

# palindrom = ''
# for i in range(len(slowo)-1,-1,-1):
#     palindrom = palindrom + slowo[i]
# print(palindrom)

# def reverse(slowo):
#     reversslowo = ''
#     i = len(slowo)
#     while i > 0:
#         reversslowo = reversslowo + slowo[i - 1]
#         i = i -1
#     return reversslowo
# print(reverse(slowo))

# reverse=''
# for i in range(1,len(slowo)+1):
#     reverse = reverse + slowo[-i]
# print(reverse)
