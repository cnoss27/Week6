library_members = []

from tkinter import *
from tkinter import messagebox

def RegisterMember(library_members, inputted_member_name):
    library_members.append(inputted_member_name.get())
    messagebox.showinfo(None, f"{inputted_member_name.get()} has been successfully registered.")
    return library_members


def FindMember(library_members, inputted_member_name):
    if inputted_member_name.get() in library_members:
        messagebox.showinfo(None, "This member is registered.")
    else:
        messagebox.showinfo(None, "No, this member is not registered.")