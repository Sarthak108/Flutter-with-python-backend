from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

# @app.post("/")
# async def test(request : Request ) :
#     print(( await request.body()).decode())
#     return "Hello World"

# /////////////////////////////////////////////////////////////////

class Test(BaseModel):
    name : str
    age : int

@app.post("/")
async def test(request : Test ) :
    print(request)
    if(request):
        return "Status 200"
    else:
        return "Status 400"
        