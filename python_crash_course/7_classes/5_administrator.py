"""This program tests the use of composition to from the user clasee. Priviledges 
is used an attribue in user"""

from admin import Admin

tola = Admin("Tola", "Martins", 45, "System Administrator", "Male", "Chess")
tola.priviledges.show_priviledges()
