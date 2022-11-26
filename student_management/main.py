import uvicorn

from fastapi import FastAPI

from student_management.model.user import User
from student_management.service.role_service import RoleService
from student_management.service.user_service import UserService

app = FastAPI()


@app.get("/roles")
def get_roles():
    """
    > This function fetches all the roles from the database
    :return: A list of roles
    """
    roles = RoleService()
    return roles.fetch_role()


@app.get("/users")
def get_users():
    """
    > This function fetches all the users from the database and returns them
    :return: A list of dictionaries
    """
    users = UserService()
    return users.fetch_user()


@app.post("/users")
def add_user(user: User):
    users = UserService()
    response = users.add_user(user)
    if response is not None:
        return f"{user.name} is successfully added!!!"
    else:
        return f"Failed :( Please try again!!"

# A special condition that gets executed only when you run the Python file from the command line.
if __name__ == "__main__":
    # # Calling the `display_welcome_sms` and `get_application_inputs` methods of the `View` class.
    # View.display_welcome_sms()
    # View.get_application_inputs()
    uvicorn.run("main:app", host='127.0.0.1', port=4500, reload=True, workers=3)
