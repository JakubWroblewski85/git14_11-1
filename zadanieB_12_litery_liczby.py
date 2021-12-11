
string_user = ("hello world! 123")

def ilosc_cyft_i_liter(string_user):
    string = number = 0
    for i in string_user:
        if i.isdigit():
            number = number + 1
        elif i.isalpha():
            string = string + 1
    return string, number

string, number = ilosc_cyft_i_liter(string_user)
print("LITERY", string)
print("CYFRY ", number)
