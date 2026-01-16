from fastapi.templating import Jinja2Templates

BoardDB_NAME = "board.db"
MemberDB_NAME = "member.db"
SungJukDB_NAME = "sungjuk.db"

templates = Jinja2Templates(directory="templates")