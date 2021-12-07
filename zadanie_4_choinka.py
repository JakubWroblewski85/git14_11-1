
height = int(input('''Podaj wysokość choinki jaką chcesz narysować.
Gdzie cyfra 1 odzwierciedla jedną '*' w góre. Podaj jak wysoką choinke chcesz na Święta'''))
starts = 1

for i in range(height):
    print((' ' * (height - i)) + ('*' * starts))
    starts += 2
print((' ' * height) + '|')




