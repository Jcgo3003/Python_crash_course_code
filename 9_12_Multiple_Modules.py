# 9-12. Multiple Modules: Store the User class in one module, and store 
# the Privileges and Admin classes in a separate module. In a separate 
# file, create an Admin instance and call show_privileges() to show that 
# everything is still working correctly.

import user
import admin


test = user.User("John", "Lennon")
test.greet_user()

test2 = admin.Admin("Yoko", "Onno")
test2.greet_user()
test2.privileges.show_privileges()