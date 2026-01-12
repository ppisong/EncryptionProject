# 비즈네르 암호는 시저 암호를 26가지 다른 버전으로 만든 것
# 시저 암호 :알파벳을 몇 칸 옆으로 밀어서 바꿈
# 키 : 얼마나 밀지 알려주는 중요한 비밀단어
# 항상 순방향으로 움직이는데 비즈네르 암호에서는 방향이 중요하지 않음
# 변수는 키가 중요
# 알파벳만 대상, 대문자만 대상

def vigenere_cipher(text, key, encrypt=True):
    cipher_text = ''
    key_index = 0  # 키의 위치
    # key = key.upper()  # 계산을 쉽게 하기 위해 대문자로 통일
    # 키는 소문자로 입력 권유한 뒤 shift에서는 97 적용

    for char in text:
        if char.isalpha(): # 문자가 알파벳인지 체크
            if (key[key_index % len(key)]) == ' ':key_index += 1 # 공백은 건너뜀
            shift = ord(key[key_index % len(key)]) - 97


            if not encrypt:   # '복호화중이라면'이라면 반대로 당김
                shift *= -1

            if char.islower():
                cipher_text += chr((ord(char) - 97 + shift) % 26 + 97)
            elif char.isupper():
                cipher_text += chr((ord(char) - 65 + shift) % 26 + 65)

            key_index += 1 # 다음 암호화에 쓸 키를 위해 키 인덱스 증가

        else:
            cipher_text += char


    return(cipher_text)

if __name__ == '__main__':
    plain_text = 'wish to be free from myself'
    secret_key = 'secret is beautiful'

    encrypted = vigenere_cipher(plain_text, secret_key)
    print(encrypted)
    decrypted = vigenere_cipher(plain_text, secret_key, encrypt=False )
    print(decrypted)
