def caesar_cipher(text, shift, left=True):
    cipher_text = ' '
    if not left:
        shift *= -1
    # 26을 넘어가면 left로 움직이는 것이 아니라 부호가 바뀐다
    for char in text:
        if char.islower():
            cipher_text += chr((ord(char) - 97 + shift) % 26 + 97)
        elif char.isupper():
            cipher_text += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            cipher_text += char


    return(cipher_text)


if __name__ == '__main__':
    text = "hello world"
    # encrypted = caesar_cipher(text, 3, True)
    encrypted = caesar_cipher(text, 3)
    print(encrypted)
    decrypted = caesar_cipher(encrypted, 3,False)
    print(decrypted)

    text = "HELLO WORLD"
    encrypted = caesar_cipher(text, 3)
    print(encrypted)
    decrypted = caesar_cipher(encrypted, 3, False)
    print(decrypted)

    text = "Hello World"
    encrypted = caesar_cipher(text, 3)
    print(encrypted)
    decrypted = caesar_cipher(encrypted, 3, False)
    print(decrypted)

