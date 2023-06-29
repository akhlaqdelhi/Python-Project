#  it an exmaple file for dictinary and tuples
def fn_dictionry_one():
    address = {"Address1": "Street no 123", "City": "SRE", "State": "UP"}
    print("City== "+address["City"])
    if "State" in address:
        print("State key found in the dictionary")

    if "pin" not in address:
        print("pin key is not in address dictionary")


def fn_dictionry_student():
    student = {"Name": "Ajay", "Age": "23", "Course": "Diploma"}
    for k, v in student.items():
        print("Key= "+k+" | value= "+v)


def fn_tuples1():
    cities = ("SRE", "JALALABAD", "MEERUT", "NAJIBABAD", "GHAZIUABAD", "LUCKNOW", "ALAHABAD", "MORADABAD", "AJMER", "New Delhi")
    for city in cities: # iterating tuple vlues using a for loop
        print(city)

    index = 0
    while index < len(cities):
        print(str(index+1)+" cityName = "+cities[index])
        index += 1


def fn_tuple_slicing():
    int_num = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    slice1 = int_num[1:5]   # strt from index to 1 less than 5(4), here 1st index is included but end index is not included == (2, 3, 4, 5)
    print(slice1)
    print(int_num[:5])  # start from begining and end at index 1les than 5(4) == (1, 2, 3, 4, 5)
    print(int_num[7:])  # start from index 7 and go till end == (8, 9, 10)
    print(int_num[:])  # start from begining and go till end == (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(int_num[0:7:2])  # start from index 0 and updato index number 1 less than 7 at an interval of 2 == (1, 3, 5 ,7)
    print(int_num[:9:3])  # start from begining and updato index number 1 less than 9 at an interval of 2 == (1, 4, 7)


def fn_tuple_mixed():
    tuple_mix = (1, 2, (23, "Name", True), "Hello", 154.65)
    print(tuple_mix[2])   # fetch inside tuple == (23, 'Name', True)
    print(tuple_mix[2][1])   # fetch  == Name


def fn_tuple_count():
    marks = (90, 91, 98, 95, 90, 98, 90)
    print(marks.count(90))  # count how many time the value 90 repeat in tuples
    idx = marks.index(98)
    print(idx)      # find first accurence index num == 2

# fn_dictionry_one()

# fn_dictionry_student()

# fn_tuples1()

# fn_tuple_slicing()

# fn_tuple_mixed()

fn_tuple_count()