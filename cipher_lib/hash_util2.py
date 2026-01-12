# pip install pycryptodome

import hashlib

def get_filehash(file):
    # if절 이하 파일 경로 통해 파일 받아 매개변수로 사용
    # 해시알고리즘 초기화
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()

    # 해시알고리즘 적용전 파일내용을 바이너리로 한번에 읽음 - 저용량 파일
    # md5.update(open(file , 'rb').read())
    # sha1.update(open(file, 'rb').read())
    # sha256.update(open(file,'rb').read())

    # binary_readed = open(file, 'rb').read()
    # md5.update(binary_readed)
    # sha1.update(binary_readed)
    # sha256.update(binary_readed)

    #해시알고리즘 적용전 파일내용을 청크chunk 단위(조각으로 나눠서)로 읽음 - 대용량 파일
    with open(file, 'rb') as f:
         # 파일은 8192씩 나눠 하나씩 읽어들인다.
            # 더 이상 읽어들일 게 없으면 b'' 빈 바이트 반환.
            # lambda는 인자 없은 함수로 호출될 때마다 다음 8192 읽음
            # 청크의 장점 - 메모지 절약, 스티리밍 처리
            # iter(lambda: f.read(8192), b'') ->[청크][청크][청크}... #8KB
        for chunk in iter(lambda: f.read(65536), b''): #64KB
            md5.update(chunk)
            sha1.update(chunk)
            sha256.update(chunk)

    # 디지털지문 생성
    md5digest = md5.hexdigest()
    sha1digest = sha1.hexdigest()
    sha256digest = sha256.hexdigest()

    return md5digest, sha1digest, sha256digest

if __name__ == '__main__':
    file_path = 'c:/Java/BIND9.16.50.x64.zip'
    md5hashed, sha1hashed, sha256hashed = get_filehash(file_path)
    print(md5hashed)
    print(sha1hashed)
    print(sha256hashed)

