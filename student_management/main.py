from model.role import Role, Roles
from pprint import pprint
from service.role_service import RoleService

if __name__ == "__main__":
    print(f"{4*'*'} Student Managment System {4*'*'}")
    print("Please select the below option: ")
    print("1. Manage Role")
    print("2. Manage Users")
    print("3. Exit")

    role_service = RoleService()
    while(True):
        root_manage = int(input("Enter either (1) OR (2) OR (3): "))
        print(root_manage)
        if root_manage == 1:
            print("Please select the below option to manage roles: ")
            print("1. Add Role")
            print("2. Delete Role")
            print("3. Update Role")
            print("4. Search Role")
            print("5. Fetch All Roles")
            print("6. Exit")
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
                    pass
                case 5:
                    pass
                case other:
                    pass
        elif root_manage == 2:
            pass
        else:
            break