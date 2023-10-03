library_members = []

def RegisterMember(library_members):
    library_members.append(input("What is the name of the new member? Input it here:"))


def FindMember(library_members):
    name = input("What is the name of the person you are searching for? Input it here:")
    if name in library_members:
        print(f"Yes, {name} is a registered member.")
    else:
        print("That name is not registered yet")