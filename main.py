from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    email: str
    age: int


users = []


@app.get("/users")
def get_users():
    return users


@app.post("/users")
def create_user(user: User):
    data = user.model_dump()

    data["id"] = len(users) + 1

    users.append(data)

    return data


@app.get("/users/{user_id}")
def get_user(user_id: int):

    for user in users:
        if user["id"] == user_id:
            return user

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )


@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):

    for existing_user in users:

        if existing_user["id"] == user_id:

            existing_user["name"] = user.name
            existing_user["email"] = user.email
            existing_user["age"] = user.age

            return existing_user

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )


@app.delete("/users/{user_id}")
def delete_user(user_id: int):

    for user in users:

        if user["id"] == user_id:

            users.remove(user)

            return {
                "message": "User deleted"
            }

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )