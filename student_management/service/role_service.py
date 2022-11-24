from model.settings import Settings
from pydantic import parse_obj_as
from model.role import Roles
from model.role import Role

class RoleService():

    '''
        Add - add the role
        Delete - delete the role
        Update - update the role
        Get - fetch the role
        Search - search the role
    '''

    def __init__(self):
        try:
            with open(Settings().role_sample_path) as file:
                roles_from_file = file.read() # Read from json file
                self.roles = Roles.parse_raw(roles_from_file) # Convert json to pydantic
        except Exception as e:
            print("Oops!", e, "occurred.")
            print("Next entry.")

    '''
        Add the role 
    '''
    def add_role(self, role_id, role_name, role_description):
        role = Role(
            role_id=role_id, 
            role_name=role_name, 
            role_description=role_description)
        self.roles.__root__.append(role)
        return self.roles

    '''
        Remove the role 
    '''
    def delete_role(self, role_id):
        selected_roles = [index for index, role in enumerate(self.roles.__root__) if role.role_id == int(role_id)]
        del self.roles.__root__[selected_roles[0]]
        return self.roles

    '''
        Update the role 
    '''
    def update_role(self, role_id, role_name, role_description):
        selected_roles = [index for index, role in enumerate(self.roles.__root__) if role.role_id == int(role_id)]
        self.roles.__root__[selected_roles[0]].role_name = role_name 
        self.roles.__root__[selected_roles[0]].role_description = role_description 
        return self.roles