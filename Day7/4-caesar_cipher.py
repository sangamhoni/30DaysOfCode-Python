alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypter(text, shift):
    text_list=list(text)
    for letter in range(len(text_list)):
        for alpha in range(len(alphabet)):
            if text_list[letter]==alphabet[alpha]:
                if (alpha<=20):
                    text_list[letter]=alphabet[alpha + shift]
                else:
                    text_list[letter]=alphabet[alpha + shift-26]
                break

    print(f"The encrypted text is {''.join(text_list)}");


def decrypter(text, shift):
    text_list=list(text)
    for letter in range(len(text_list)):
        for alpha in range(len(alphabet)):
            if text_list[letter]==alphabet[alpha]:
                if (alpha<=20):
                    text_list[letter]=alphabet[alpha - shift]
                else:
                    text_list[letter]=alphabet[alpha - shift]
                break

    print(f"The decrypted text is {''.join(text_list)}");

# Instead of this, you can simply use .index() to know the position of the string in the list

to_do=input("Type 'encrypt' to encrypt and 'decrypt' to decrypt: \n").lower()
text=input("Type your message: \n").lower()
shift_no=int(input("Type your shift number: \n"))

if (to_do=='encrypt'):
    encrypter(text=text, shift=shift_no)
elif (to_do=='decrypt'):
    decrypter(text=text, shift=shift_no)
