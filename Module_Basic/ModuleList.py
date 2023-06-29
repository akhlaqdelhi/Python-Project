
def fn_listbasics():
    name_list = ["Ahmed", "khalid", "saleem", "sajid", "naeem", "mahboob"]
    validate_value = "sajid" in name_list
    print("whether sajid in list== "+str(validate_value))
    validate_value = "Amir" not in name_list
    print("whether Amir not in list== "+str(validate_value))
    for val in name_list:
        print("list value is= "+val)
# -----------------------------------------------


def fn_more_list():
    userList = ["one", "two", "three", "four"]
#     add one more vaue at end
    print(" intial list== "+str(userList))
    userList.append("five")
    print("after append list== " + str(userList))
    userList.remove("three")
    print("after remove list== " + str(userList))
    userList.insert(2, "teen")
    print("after insert list== " + str(userList))
    userList.sort()
    print("after sorting list== " + str(userList))
    userList.sort(reverse=True)
    print("after sorting reverse list== " + str(userList))

# ------------- calling to base code
# fn_listbasics()

fn_more_list()