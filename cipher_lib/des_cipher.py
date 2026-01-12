# DES : 64 비트 블록, 56 비트 키
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# 키 설정(8바이트 - 8자)
key = b'warcraft'

# 평문
plaintext =b'Hello, world!!'

# 패딩 - 데이터 길이를 맞추기 위해 덧붙이는 값
padded_text = pad(plaintext,8)
# 암호화 - 블록단위 암호화 지원 모드(ECB)
des = DES.new(key, DES.MODE_ECB)
encrypted = des.encrypt(padded_text)
print(encrypted)

# 복호화
decrypted = des.decrypt(encrypted)
unpad_decrypted = unpad(decrypted,8)
print(unpad_decrypted)

# import inspect
# import Crypto.Cipher.DES as DES
#
# print(inspect.getsource(DES))
