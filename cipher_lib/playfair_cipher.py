# 평문 : be careful for assassinator
# 변환 : be ca re fu lf or as sa sx si na to rx(같은 글자 중복될 때와 마지막에 x)
# 실제 키 : assassinator
# 암호화 테이블 : asint arbcd efghj klamz uvwxy
# 키 2 : secret is beautiful
# 암호문 :
from importlib.metadata import pass_none


def prepare_text(text):
    ptext = []
    pos = 0

    # 공백 제거, 소문자 일괄변환
    text = text.replace(' ', '').lower()

    # 2글자씩 잘라서 diagram으로 생성
    # while pos < len(text):
    #     first = text[pos]
    #     second = text[pos + 1]
    #     ptext.append(first + second)
    #     pos = pos + 2

    # while pos < len(text):
    #     first = text[pos]
    #     second = text[pos + 1]
    #
    #     if first != second:
    #         ptext.append(first + second)
    #         pos = pos + 2
    #     else:
    #         ptext.append(first)
    #         pos = pos + 1

    while pos < len(text):
        first = text[pos]
        # 마지막 문자 여부 체크
        if pos + 1 < len(text):
            second = text[pos + 1]
        else:
            second = 'x'

        if first != second:
            ptext.append(first + second)
            pos = pos + 2
        else:
            ptext.append(first + 'x')
            pos = pos + 1

    print(ptext)
    return ptext

# def prepare_text():
# text = "be careful for assassinator"
# text = text.replace(" ", "")
# result = []
# i = 0
#
# while i < len(text):
#     first = text[i]
#
#     if i + 1 < len(text):
#         second = text[i + 1]
#
#         if first == second:
#             result.append(first + 'x')
#             i += 1   # 한 글자만 소비
#         else:
#             result.append(first + second)
#             i += 2
#     else:
#     # 마지막 한 글자 남았을 때
#         result.append(first + 'x')
#         i += 1
#
# print(result)


def create_playfair_matrix(key):
    import string
    key_matrix = []
    keys = []
    # alpha = 'abcdefghijklmnopqrstuvwxyz'
    alphas = string.ascii_lowercase.replace('z','q')

    # 먼저 키를 테이블에 저장하고(단 중복을 제외)
    for ch in key:
        if ch not in keys:
            keys.append(ch)

    # 나머지 테이블 공간에 알파벳을 채움(단 중복을 제외)
    while len(keys) < 25:
        for ch in alphas:
            if ch not in keys:
                keys.append(ch)
    # print(keys, len(keys))

    # 5개씩 나눠 암호화 테이블에 저장
    # key_matrix.append(keys[0:5])
    # key_matrix.append(keys[5:10])
    # key_matrix.append(keys[10:15])
    # key_matrix.append(keys[15:20])
    # key_matrix.append(keys[20:25])

    for i in range(0, 25, 5):
        key_matrix.append(keys[i:i+5])

    print(key_matrix)
    return key_matrix



# 암호화 테이블에서 특정 문자의 위치를 알아냄
def find_pos(table,ch):

    for r in range(5):
        for c in range(5):
            if table[r][c] == ch:
                return (r,c)
# table은 리스트 속에 있는 하나의 문자를 의미

# def playfair_encript(pairs, table):
#     encrypted = []
#
#
#     for pair in pairs:
#         a, b = pair # 변수 split
#         print(a, b)
#
#         # 암호화 테이블에서 해당 문자의 위치 검색
#         # print(table[0][0], table[0][1], table[0][2], table[0][3],table[1][4])
#         # for r in range(5):
#         #     for c in range(5):
#         #         # print(table[r][c],end=' ')
#         #         if table[r][c] == a:print(a,r,c)
#         #     print()
#
#         # for r in range(5):
#         #     for c in range(5):
#         #         if table[r][c] == a:print(a,r,c)
#         #         if table[r][c] == b:print(b,r,c)
#         r1, c1 = find_pos(table,a)
#         r2, c2 = find_pos(table,b)
#         print(a, r1, c1)
#         print(b, r2, c2)
#
#         # 같은 행 : 오른쪽 다음 열 문자 선택
#         if r1 == r2:
#             code = table[r1][(c1+1) % 5] + table[r2][(c2+1) % 5]
#
#         elif c1 == c2:
#             code = table[(r1 + 1) % 5][c1] + table[(r2 +1) % 5][c2]
#         else:
#             code = table[r1][c2] + table[r2][c1]
#
#         encrypted.append(code)
#
#     # print(encrypted)
#     return encrypted


        # 같은 열 : 아래쪽 다음 문자 선택

        # 다른 행/열:같은 행에서 상대쪽 열 문자 선택

# def playfair_encript(text, key):
#     pairs = prepare_text()
#     matrix = create_playfair_matrix()
#     for pairs in pairs:
#         first = pairs[0]
#         second = pairs[1]
#         for first, second in pairs:
#             for r in range(5):
#                 for c in range(5):
#                     if matrix[r][c] == first:
#                         return (f"{char} → ({r}, {c})")
#                         found = True
#                         break
#                 if found:
#                     break
#     for char in text and char in metrix:
#         char1 = matrix[row1][col2]
#         char2 = matrix[row2][col1]
#         return (
#             matrix[(r1 + 1) % 5][c1],
#             matrix[(r2 + 1) % 5][c2]
#         )
#
#         cipher1 = matrix[(row1 + 1) % 5][col1]
# cipher2 = matrix[(row2 + 1) % 5][col2]
# return (
#     matrix[(r1 + 1) % 5][c1],
#     matrix[(r2 + 1) % 5][c2]
# )
#
#         cipher1 = matrix[row1][(col1 + 1) % 5]
# cipher2 = matrix[row2][(col2 + 1) % 5]
# return (
#     matrix[r1][(c1 + 1) % 5],
#     matrix[r2][(c2 + 1) % 5]
# )

def playfair_encript(pairs, table,encrypt=True):
    encrypted = []
    shift = 1 if encrypt else -1


    for pair in pairs:
        a, b = pair # 변수 split
        print(a, b)

        # 암호화 테이블에서 해당 문자의 위치 검색
        # print(table[0][0], table[0][1], table[0][2], table[0][3],table[1][4])
        # for r in range(5):
        #     for c in range(5):
        #         # print(table[r][c],end=' ')
        #         if table[r][c] == a:print(a,r,c)
        #     print()

        # for r in range(5):
        #     for c in range(5):
        #         if table[r][c] == a:print(a,r,c)
        #         if table[r][c] == b:print(b,r,c)
        r1, c1 = find_pos(table,a)
        r2, c2 = find_pos(table,b)
        print(a, r1, c1)
        print(b, r2, c2)

        # 같은 행 : 오른쪽 다음 열 문자 선택
        if r1 == r2:
            code = table[r1][(c1+shift) % 5] + table[r2][(c2+shift) % 5]

        elif c1 == c2:
            code = table[(r1 + shift) % 5][c1] + table[(r2 +shift) % 5][c2]
        else:
            code = table[r1][c2] + table[r2][c1]

        encrypted.append(code)

    # print(encrypted)
    return encrypted


if __name__ == '__main__':
    plain_text = 'be careful for assassinator'
    #plain_text = 'be#careful#for#assassinator'
    key = 'assassinator'

    pairs = prepare_text(plain_text)
    table = create_playfair_matrix(key)
    encrypted = playfair_encript(pairs, table)
    print(encrypted)

    decrypted = playfair_encript(encrypted, table, False)
    # 리스트의 개별문자를 모아서(join) 출력
    decrypted = "".join(decrypted).replace('x', '')
    print(decrypted)