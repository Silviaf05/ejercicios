def palindrome(word):
    word = word.replace(' ', '')
    word = word.lower()
    word_invertida = word[::-1]
    if word == word_invertida:
        return True
    else:
        return False


def run():
    word = input("Escribe una word: ")
    es_palindrome = palindrome(word)
    if es_palindrome == True:
        print("Es palindrome")
    else:
        print("No es palindrome")

if __name__ == '__main__':
    run()
