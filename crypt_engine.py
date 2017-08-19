import re

alphabetEn = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
              "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alphabetRu = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л",
              "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш",
              "щ", "ъ", "ы", "ь", "э", "ю", "я"]
En = "[a-z|A-Z]"
Ru = "[а-я|А-Я|ё|Ё]"


def encrypt(text, layout, alphabet, key):
    encrypt_string = ""
    for word in text:
        if re.match(layout, word):
            if word.islower():
                try:
                    encrypt_string += alphabet[alphabet.index(word) + key]
                except IndexError:
                    differ = len(alphabet) - alphabet.index(word)
                    encrypt_string += alphabet[-len(alphabet) + (key - differ)]
            else:
                try:
                    encrypt_string += alphabet[alphabet.index(word.lower()) +
                                               key].upper()
                except IndexError:
                    differ = len(alphabet) - alphabet.index(word.lower())
                    encrypt_string += alphabet[-len(alphabet) +
                                               (key - differ)].upper()
        else:
            encrypt_string += word
    return encrypt_string


def decrypt(text, layout, alphabet, key):
    decrypt_string = ""
    for word in text:
        if re.match(layout, word):
            if word.islower():
                try:
                    decrypt_string += alphabet[alphabet.index(word) - key]
                except IndexError:
                    differ = len(alphabet) - alphabet.index(word)
                    decrypt_string += alphabet[-len(alphabet) - (key + differ)]
            else:
                try:
                    decrypt_string += alphabet[alphabet.index(word.lower()) -
                                               key].upper()
                except IndexError:
                    differ = len(alphabet) - alphabet.index(word.lower())
                    decrypt_string += alphabet[-len(alphabet) -
                                               (key + differ)].upper()

        else:
            decrypt_string += word
    return decrypt_string
