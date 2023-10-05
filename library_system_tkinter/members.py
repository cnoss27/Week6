library_members = []

from tkinter import *
from tkinter import messagebox

def RegisterMember(library_members):
    MemberRegMenu = Tk()

    def SubmitMember():
        library_members.append(inputted_name.get())
    Label(MemberRegMenu, text="Register Member").grid(column=0, row=0)
    Label(MemberRegMenu, text="Input new members name below:").grid(column=0, row=1)
    inputted_name = Entry(MemberRegMenu)
    inputted_name.grid(column=0, row=2)
    Button(MemberRegMenu, text="Submit name", command = SubmitMember).grid(column=0, row=3)
    Button(MemberRegMenu, text="Stop registering members", command=MemberRegMenu.destroy).grid(column=0, row=4)
    MemberRegMenu.mainloop()
    return library_members


def FindMember(library_members):
    MemberCheckMenu = Tk()

    def SubmitMember():
        if inputted_name.get() in library_members:
            messagebox.showinfo(None, "This member is registered.")
        else:
            messagebox.showinfo(None, "No, this member is not registered.")
    Label(MemberCheckMenu, text="Check Member").grid(column=0, row=0)
    Label(MemberCheckMenu, text="Input desired members name below:").grid(column=0, row=1)
    inputted_name = Entry(MemberCheckMenu)
    inputted_name.grid(column=0, row=2)
    Button(MemberCheckMenu, text="Submit name", command = SubmitMember).grid(column=0, row=3)
    Button(MemberCheckMenu, text="Stop registering members", command=MemberCheckMenu.destroy).grid(column=0, row=4)
    MemberCheckMenu.mainloop()