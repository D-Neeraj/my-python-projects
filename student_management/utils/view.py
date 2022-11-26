from pprint import pprint

from student_management.model.settings import Settings
from student_management.service.role_service import RoleService
from student_management.service.user_service import UserService


class View:
    @staticmethod
    def display_select_role_option():
        """
        It displays the options to manage roles.
        :return: A string is being returned.
        """

        return Settings().select_role_option_text

    @staticmethod
    def display_welcome_sms():
        """
        It returns a string that contains a welcome message for the user
        :return: A string
        """
        return Settings().welcome_sms_text

    @staticmethod
    def display_select_user_option():
        """
        It displays a menu of options to the user.
        :return: A string is being returned.
        """
        return Settings().select_user_option_text

    @staticmethod
    def get_application_inputs():
        """
        It takes user input and calls the appropriate service function
        """
        role_service = RoleService()
        user_service = UserService()
        while True:
            root_manage = int(input("Enter either (1) OR (2) OR (3): "))
            print(root_manage)
            if root_manage == 1:
                print(View.display_select_role_option())
                role_option = int(input("Please select the option from 1..6: "))
                match role_option:
                    case 1:
                        role_id = input("Enter the id of the role: ")
                        role_name = input("Enter the name of the role: ")
                        role_description = input("Enter the description of the role: ")
                        roles = role_service.add_role(role_id, role_name, role_description)
                        pprint(roles.dict())
                    case 2:
                        role_id = input("Enter the id of the role to delete: ")
                        roles = role_service.delete_role(role_id)
                        pprint(roles.dict())
                    case 3:
                        role_id = input("Enter the id of the role: ")
                        role_name = input("Enter the name of the role: ")
                        role_description = input("Enter the description of the role: ")
                        roles = role_service.update_role(role_id, role_name, role_description)
                        pprint(roles.dict())
                    case 4:
                        search_string = input("Please enter your search query: ")
                        roles = role_service.search_role(search_string=search_string)
                        pprint(roles)
                    case 5:
                        roles = role_service.fetch_role()
                        pprint(roles)
                    case other:
                        pass
            elif root_manage == 2:
                print(View.display_select_user_option())
                user_option = int(input("Please select the option from 1..6: "))
                match user_option:
                    case 1:
                        id = input("Enter the id of the user: ")
                        name = input("Enter the name of the user: ")
                        age = input("Enter the age of the user: ")
                        gender = input("Enter the gender of the user:")
                        address = input("Enter the address of the user:")
                        religion = input("Enter the religion of the user:")
                        caste = input("Enter the caste of the user:")
                        role_id = input("Enter the role_id of the user:")
                        dob = input("Enter the dob of the user:")
                        users = user_service.add_user(id, name, age, gender, address, religion, caste, role_id, dob)
                        pprint(users.dict())
                    case 2:
                        id = input("Enter the id of the user to delete: ")
                        users = user_service.delete_user(id)
                        pprint(users.dict())
                    case 3:
                        id = input("Enter the id of the user: ")
                        name = input("Enter the name of the user: ")
                        age = input("Enter the age of the user: ")
                        gender = input("Enter the gender of the user:")
                        address = input("Enter the address of the user:")
                        religion = input("Enter the religion of the user:")
                        caste = input("Enter the caste of the user:")
                        role_id = input("Enter the role id of the user:")
                        dob = input("Enter the DOB of the user:")
                        users = user_service.update_user(id, name, age, gender, address, religion, caste, role_id, dob)
                        pprint(users.dict())
                    case 4:
                        search_string = input("Please enter your search query: ")
                        users = user_service.search_user(search_string=search_string)
                        pprint(users)
                    case 5:
                        users = user_service.fetch_user()
                        pprint(users)
                    case other:
                        pass
            else:
                break
