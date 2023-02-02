from fastapi import FastAPI, Depends
from fastapi import params
import uvicorn
app = FastAPI()

def user_login(name: str = params, password: str = params):
    return {"name": name, "valid": True}

@app.get("/user")
def get_user(user: dict = Depends(user_login)) -> dict:
    return user

if __name__ == "__main__":
     uvicorn.run("depends:app")