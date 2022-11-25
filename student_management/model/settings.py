from pydantic import BaseSettings

'''
It's a class that inherits from the BaseSettings class and has two attributes that 
are the paths to the sample role and
'''


class Settings(BaseSettings):
    role_sample_path = r"C:\Users\Welcome\python projects\student_management\data\sample_role.json"
    user_sample_path = r"C:\Users\Welcome\python projects\student_management\data\sample_users.json"
    select_role_option_text = f"""Please select the below option to manage roles:\n
                    1. Add Role\n
                    2. Delete Role\n
                    3. Update Role\n
                    4. Search Role\n
                    5. Fetch Role\n
                    6. Exit"""
    welcome_sms_text = f"""
                f"{4 * '*'} Student Management System {4 * '*'}"
                    Please select the below option:  \n
                    1. Manage Role \n
                    2. Manage Users \n
                    3. Exit \n
                """
    select_user_option_text = """Please select the below option to manage users:\n
                    1. Add User\n
                    2. Delete User\n
                    3. Update User\n
                    4. Search User\n
                    5. Fetch User\n
                    6. Exit"""
