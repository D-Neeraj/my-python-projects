from pydantic import BaseSettings

'''
It's a class that inherits from the BaseSettings class and has two attributes that 
are the paths to the sample role and
'''


class Settings(BaseSettings):
    role_sample_path = r"C:\Users\Welcome\python projects\student_management\data\sample_role.json"
    user_sample_path = r"C:\Users\Welcome\python projects\student_management\data\sample_users.json"
    select_role_option_text = f"""Please select the below option to manage roles:
1. Add Role
2. Delete Role
3. Update Role
4. Search Role
5. Fetch Role
6. Exit
"""
    welcome_sms_text = f"""
{4 * '*'} Student Management System {4 * '*'}
Please select the below option:  
1. Manage Role 
2. Manage Users 
3. Exit 
                """
    select_user_option_text = """Please select the below option to manage users:
1. Add User
2. Delete User
3. Update User
4. Search User
5. Fetch User
6. Exit
                    """
