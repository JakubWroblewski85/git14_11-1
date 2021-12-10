
# lista_user = input("Podaj przykładową listę, wyliczymy ile razy w niej jest cyfra 4...\n")
lista_user = 1,2,3,4,5,6,7,65,4,34,23,45,4

def lista_count(lisa_user):
    count = 0
    for liczba in lista_user:
        if liczba == 4:
            count += 1
    return count

print(lista_count(lista_user), "-razy masz cyfre 4 w swojej liscie")