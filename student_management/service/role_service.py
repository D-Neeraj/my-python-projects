


# > This class is responsible for managing roles
from student_management.model.role import Roles, Role
from student_management.model.settings import Settings


class RoleService:

    def __init__(self):
        """
        If the file exists, read the file and convert the json to pydantic
        """
        try:
            with open(Settings().role_sample_path) as file:
                roles_from_file = file.read()  # Read from json file
                self.roles = Roles.parse_raw(roles_from_file)  # Convert json to pydantic
        except Exception as e:
            print("Oops!", e, "occurred.")

    def add_role(self, role_id, role_name, role_description):
        """
        It adds a role to the roles list

        :param role_id: The unique identifier for the role
        :param role_name: The name of the role
        :param role_description: A description of the role
        :return: The roles object.
        """

        role = Role(
            role_id=role_id,
            role_name=role_name,
            role_description=role_description)
        self.roles.__root__.append(role)
        return self.roles

    def delete_role(self, role_id):
        """
        It deletes a role from the roles list

        :param role_id: The ID of the role you want to delete
        :return: The roles.
        """
        selected_roles = [index for index, role in enumerate(self.roles.__root__) if role.role_id == int(role_id)]
        del self.roles.__root__[selected_roles[0]]
        return self.roles

    def update_role(self, role_id, role_name, role_description):
        """
        It takes the role_id, role_name, and role_description as arguments, and then updates the role_name and
        role_description of the role with the matching role_id

        :param role_id: The id of the role to be updated
        :param role_name: The name of the role
        :param role_description: The description of the role
        :return: The updated role.
        """

        selected_roles = [index for index, role in enumerate(self.roles.__root__) if role.role_id == int(role_id)]
        self.roles.__root__[selected_roles[0]].role_name = role_name
        self.roles.__root__[selected_roles[0]].role_description = role_description
        return self.roles

    def fetch_role(self):
        """
        It returns the role of the user
        :return: The root role of the roles object.
        """
        return self.roles.__root__

    def search_role(self, search_string):
        """
        If the search string is numeric, return a list of roles where the role id is equal to the search string or the role
        name contains the search string. Otherwise, return a list of roles where the role name contains the search string

        :param search_string: The string to search for
        :return: A list of roles that match the search string.
        """

        if search_string.isnumeric():  
            return [role for role in self.roles.__root__ if role.role_id == int(search_string) or role.role_name.__contains__(search_string)]
        else:
            return [role for role in self.roles.__root__ if role.role_name.__contains__(search_string)]



