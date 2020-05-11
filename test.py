import random

# data = open('data.txt', 'r+')

def add_staff():
    global staff_list, code, code_list

    staff_amount = int(input('Nhập số lượng nhân viên: '))

    code_list = []
    staff_list = []
    temp_staff_list = []
    for i in range(staff_amount):
        temp_staff_list = []
        name = str(input('Nhập tên nhân viên: '))
        age = int(input('Nhập tuổi: '))
        gender = str(input('Nhập giới tính: '))

        for j in range(staff_amount):
            code = random.randint(100, 300)
            code_list.append(code)
            try:
                if code_list[i] == code_list[i + 1]:
                    code_list[i] = random.randint(100, 300)
            except:
                pass

        temp_staff_list.append(code_list[i])
        temp_staff_list.append(name)
        temp_staff_list.append(age)
        temp_staff_list.append(gender)

        staff_list.append(temp_staff_list)

    return staff_list

def find_staff_code():
    
    id = int(input('Nhập id nhân viên: '))
    for i in range(len(staff_list)):
        if id == staff_list[i][0]:
            return staff_list[i]
        else:
            temp = 'Ko có nhân viên nào mang mã' + id
            return temp

def find_name_staff():

    name = str(input('Nhập tên nhân viên muốn tìm: '))
    for i in range(len(staff_list)):
        if staff_list[i][1] == name:
            return staff_list[i]
        else:
            temp = 'Ko có nhân viên nào tên ' +  name
            return temp

def delete_all_staff():

    staff_list = []
    return 'Đã xóa hết dữ liệu nhân viên'

def print_by_gender():
    
    gender = str(input('Nhập giới tính cần in: '))
    for i in range(len(staff_list)):
        if staff_list[i][3] == gender:
            if staff_list[i][3] != None:
                print(staff_list[i])

def print_by_age():
    for i in range(len(staff_list)):
        if staff_list[i][2] in range(21, 25):
            print(staff_list[i])

n = ''
while True:

    # ở đây 
    # tại sao khi tôi thêm cái while n == '' vào thì cái def add_staff nó lại gọi ra vô hạn
    while n == '':
        try:
            n = str(input('type: '))
        except:
            n = str(input('type: '))
    if n == '1':
        print(add_staff())
    elif n == '2':
        print(find_staff_code())
    elif n == '3':
        print(find_name_staff())
    elif n == '4':
        print(delete_all_staff())
    elif n == '5':
        print(print_by_gender())
    elif n == '6':
        print(print_by_age())
    elif n == '7':
        break
    