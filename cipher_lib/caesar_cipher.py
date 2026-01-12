# 단일 치환 암호 기법의 핵심
# 영문자에 대한 ASCII 코드값 변환 :chr, ord
# print(chr(97), ord('a'))
# 치환 규칙을 수학적으로
# a -> x (right shift 3)
# print(chr((ord('a') + 23)))
# print(chr((ord('a') + 23)))

# hello world를 단일 치환법으로 암호화

# plain_text = 'hello world' # 평문
# direction = 'right'
# shift = 3
# cipher_text = ' '       # 암호문
#
# for char in plain_text:
#     base = 97  # 기준 수
#     if char == ' ':
#         cipher_text += ' '
#     elif direction == 'left':
#         cipher_text += chr((ord(char) - 97 + shift) % 26 + 97)
#     else:
#         cipher_text += chr((ord(char) - 97 - shift) % 26 + 97)
#
# print('평문', plain_text)
# print('암호문', cipher_text)

# 다른 방식
# plain_text = 'hello world'
# direction = 'right'
# shift = 3
# cipher_text = ''
#
# for char in plain_text:
#     if char == ' ':
#         cipher_text += ' '
#     elif char.isalpha():
#         base = ord('a')
#         if direction == 'left':
#             cipher_text += chr((ord(char) - base - shift) % 26 + base)
#         else:
#             cipher_text += chr((ord(char) - base + shift) % 26 + base)
#
# print('평문:', plain_text)
# print('암호문:', cipher_text)


# x = ord(input("알파벳을 입력하세요: "))
#
# if 97 <= x <= 99:
#     print(chr(x + 23))
#
# if 100 <= x <= 119:
#     print(chr(x + 3))
#
# if 119 <= x < 123:
#     print(chr(x - 13))

# def caesar_cipher1(text, dirc, shift):
#     cipher_text = ' '
#     base = 97  # 알파벳에서 소문자 시작하는 기준 수
#
#     for char in text:
#         if char == ' ':
#             cipher_text += ' '
#         elif dirc == 'left':
#             cipher_text += chr((ord(char) - 97 + shift) % 26 + 97)
#         else:
#             cipher_text += chr((ord(char) - 97 - shift) % 26 + 97)
#
#     return(cipher_text)
#
# if __name__ == '__main__':
#     plain_text = input('암호화할 문장을 입력하세요: ')
#     direction = input('이동할 방향은?(right, left): ')
#     shift = int(input('이동 횟수는?: '))
#
#     encrypted_text = caesar_cipher1(plain_text, direction, shift)
#
#     print(plain_text, encrypted_text)


def caesar_cipher2(text, dirc, shift):
    cipher_text = ' '
    base = 65  # 알파벳에서 대문자 시작하는 기준 수

    for char in text:
        if char == ' ':
            cipher_text += ' '
        elif dirc == 'left':
            cipher_text += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            cipher_text += chr((ord(char) - 65 - shift) % 26 + 65)

    return(cipher_text)

if __name__ == '__main__':
    plain_text = input('암호화할 문장을 입력하세요: ')
    direction = input('이동할 방향은?(right, left): ')
    shift = int(input('이동 횟수는?: '))

    encrypted_text = caesar_cipher2(plain_text, direction, shift)

    print(plain_text, encrypted_text)