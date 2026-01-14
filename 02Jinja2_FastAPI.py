from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.responses import HTMLResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi import Form
from cipher_lib.caesar_cipher_v2 import caesar_cipher
# 라이브러리에서 만든 함수를 가져올 때는 이렇게

# FastAPI 인스턴스 생성
app = FastAPI()

# 템플릿 엔진 설정 및 templates 폴더 경로 지정
templates = Jinja2Templates(directory="templates")

# 루트 경로("/jhello")에 GET 요청이 들어오면 실행될 함수 정의
# { : }는 딕셔너리 형식의 리턴
# @app.get("/jhello")이 앞에 달리기 때문에 이 함수는 단지 메시지를 반환하는 것외에도
# dict 형식을 json 형식으로 바꾸주는 등 코드에 보이지 않은 기능 수행
@app.get("/jhello")
def json_hello():
    return {"message": "Hello, World!"}


# 별도의 HTML 파일을 사용해서 웹 페이지를 렌더링
# 보통 Jinja2 템플릿 엔진을 사용하며, templates 폴더를 만들어 HTML 파일을 두고 렌더링
# "request": request는 클라이언트가 서버로 보낸 HTTP 요청 전체를 담은 특별한  구조적 내용을 담고 있는 변수. 개발자도구에 나오는 IP 주소 등
# 변수의 타입 : Request :의존성 주입(DI) :시스템이 정보를 집어넣어 준다
@app.get("/j2hello", response_class=HTMLResponse)
def jinja2_hello(request: Request):
    # TemplateResponse(템플릿파일명, 템플릿에_전달할_데이터)
    # 템플릿 컨텍스트 - HTML 안에서 사용할 수 있는 변수들의 집합
    # json:자바스크립트를 이용해 데이터를 표현하는 형식:파이썬의 딕셔너리 구조와 비슷: 파이선에서는 따옴표를 안쓰는데 자바에서는 쓴다
    # {}에 키:값 쌍으로 데이터들을 정의
    return templates.TemplateResponse("j2hello.html",
                                      {"request": request, "message": "Hello, World!"})

#     html_file = "j2hello.html"
#     data = {"request": request, "message": "Hello, World!"}
#     return templates.TemplateResponse(htmㅣ_file, data)
#
# GET 요청: 로그인 폼 보여주기
@app.get("/login", response_class=HTMLResponse)
def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# POST 요청: 폼 데이터 처리
@app.post("/login", response_class=HTMLResponse)
# username, password는 Form 데이터에서 문자열 타입으로 필수 입력 값이다
# username: str = Form(...) 변수타입은 str, 변수값은 Form(...)
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    # username과 password 값을 템플릿으로 전달
    form = await request.form()
    # 암호화 처리
    caesar_encrypted = caesar_cipher(password,  shift = 5)

    return templates.TemplateResponse("loginok.html", {
        "request": request, "form":form, "username": username, "password": password, "caesar_encrypted" : caesar_encrypted
    })

# get과 post의 차이. get은 form 없이 약식, post는 보안에 주의하고 form으로 보내고 긴 내용을 보낼 때
# async

# 스크립트를 직접 실행할 때만 서버 실행
# 실행 파일 속에 print(def 함수) 실행의 의미가 들어있다고 봐야 함
if __name__ == "__main__":
    import uvicorn  # uvicorn을 직접 임포트해서 사용
    uvicorn.run('02Jinja2_FastAPI:app', host="0.0.0.0", port=8000, reload=True)
