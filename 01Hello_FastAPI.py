from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, HTMLResponse

app = FastAPI()

# @app.get("/")
# async def json_hello():
#     # JSON으로 응답. JSON이 response_class의 기본값
#     return {"message": "Hello, World!"}

@app.get("/thello", response_class=PlainTextResponse)
def text_hello():
    # 텍스트로 응답
    return "Hello, World!"

@app.get("/hhello", response_class=HTMLResponse)
# 경로에 주의할 것
def html_hello():
    # html로 응답
    html_content = """
		<!DOCTYPE html>
		<html>
		    <head>
		        <title>Hello Page</title>
		    </head>
		    <body>
		        <h1>Hello, World!</h1>
		        <p>FastAPI로 만든 HTML 페이지입니다.</p>
		    </body>
		</html>
		"""
    return html_content

# 스크립트를 직접 실행할 때만 서버 실행
if __name__ == "__main__":
    import uvicorn  # uvicorn을 직접 임포트해서 사용
    uvicorn.run('01Hello_FastAPI:app', host="0.0.0.0", port=8000, reload=True)