from fastapi import FastAPI

#get post put delte patch options head trace connect

app = FastAPI()

@app.get('/hellowrold')
async def helloworld():
    return{"message":"hello world"}


@app.get('/healthcheck')
async def healthcheck():
    return{"message":"health check"}

@app.get("/readuser/{user}")
async def read_user(user:str):
    return {"message":f"user {user} retrieved successfully!"}

@app.post("/createuser/{user}")
async def create_user(user:str):
    return {"message":f"user {user} created successfully!"}

@app.put("/updateuser")
async def update_user(user:str):
    return {"message":f"user {user} updated sucessfully!"}

@app.delete("/deleteuser")
async def delete_user(user:str):
    return {"message":f"user {user} deleted succesfuuly "}