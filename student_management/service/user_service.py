from model.settings import Settings
from model.user import User
from model.user import Users


# > This class provides a service for managing users
class UserService:
    def __init__(self):
        """
        If the file exists, read the file and convert the json to pydantic
        """
        try:
            with open(Settings().user_sample_path) as file:
                users_from_file = file.read()  # Read from json file
                self.users = Users.parse_raw(users_from_file)  # Convert json to pydantic
        except Exception as e:
            print("Oops!", e, "occurred.")
            print("Next entry.")

    def add_user(self, id, name, age, gender, address, religion, caste, role_id, dob):
        """
        It adds a user to the users list

        :param id: The id of the user
        :param name: The name of the user
        :param age: Age of the user
        :param gender: 1 for male, 2 for female
        :param address: The address of the user
        :param religion: Hindu, Muslim, Christian, Sikh, Jain, Buddhist, Parsi, Other
        :param caste: Brahmin, Kshatriya, Vaishya, Shudra
        :param role_id: 1 for admin, 2 for user
        :param dob: date of birth
        :return: The users list is being returned.
        """
        user = User(
            id=id,
            name=name,
            age=age,
            gender=gender,
            address=address,
            religion=religion,
            caste=caste,
            role_id=role_id,
            dob=dob)
        self.users.__root__.append(user)
        return self.users

    def delete_user(self, id):
        """
        It deletes a user from the list of users

        :param id: The id of the user to delete
        :return: The users object is being returned.
        """
        selected_users = [index for index, user in enumerate(self.users.__root__) if user.id == int(id)]
        del self.users.__root__[selected_users[0]]
        return self.users

    def update_user(self, id, name, age, gender, address, religion, caste, role_id, dob):
        """
        It takes the id of the user to be updated, and the new values for the other attributes of the user, and updates the
        user with the new values

        :param id: The id of the user to be updated
        :param name: Name of the user
        :param age: int
        :param gender: 1 for male, 2 for female
        :param address: The address of the user
        :param religion: Hindu, Muslim, Christian, Sikh, Buddhist, Jain, Parsi, Other
        :param caste: The caste of the user
        :param role_id: 1 for admin, 2 for user
        :param dob: date of birth
        :return: The updated user object is being returned.
        """
        selected_users = [index for index, user in enumerate(self.users.__root__) if user.id == int(id)]
        self.users.__root__[selected_users[0]].name = name
        self.users.__root__[selected_users[0]].age = age
        self.users.__root__[selected_users[0]].gender = gender
        self.users.__root__[selected_users[0]].address = address
        self.users.__root__[selected_users[0]].religion = religion
        self.users.__root__[selected_users[0]].caste = caste
        self.users.__root__[selected_users[0]].role_id = role_id
        self.users.__root__[selected_users[0]].dob = dob
        return self.users

    def search_user(self, search_string):
        """
        It returns a list of users whose name contains the search string, or whose id matches the search string if it is
        numeric

        :param search_string: The string to search for
        :return: A list of users that match the search string.
        """
        if search_string.isnumeric():
            return [user for user in self.users.__root__ if
                    user.id == int(search_string) or user.name.__contains__(search_string)]
        else:
            return [user for user in self.users.__root__ if user.name.__contains__(search_string)]

    def fetch_user(self):
        """
        It returns the root user of the users tree
        :return: The root user.
        """
        return self.users.__root__
