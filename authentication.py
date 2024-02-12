def isAdminUser(user_id):
    file = open("admins.txt", "r")
    content = [int(x.strip()) for x in file.readlines()]
    file.close()
    
    if user_id in content:
        return True
    return False

def add_admin_to_file(new_admin):
    file = open("admins.txt", "a")
    file.write(f"{new_admin}\n")
