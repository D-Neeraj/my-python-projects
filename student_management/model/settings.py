from pydantic import BaseSettings


class Settings(BaseSettings):
    role_sample_path = r"C:\Users\Welcome\python projects\student_management\data\sample_role.json"
    user_sample_path = r"C:\Users\Welcome\python projects\student_management\data\sample_user.json"

