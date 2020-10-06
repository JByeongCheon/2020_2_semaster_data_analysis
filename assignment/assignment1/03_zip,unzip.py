import random

#a번
def my_zip(): #무작위 리스트 값이 입력 된 2개 생성
    limit_num1,limit_num2 = random.randint(1,10), random.randint(1,10)
    rand_list1 = []
    rand_list2 = []

    for i in range(limit_num1):
        num = random.randint(1,100) #1~100사이의 값이 리스트에 포함 된다.
        rand_list1.append(num)

    for i in range(limit_num2):
        num = random.randint(1, 100)
        rand_list2.append(num)

    return my_zip_current(rand_list1,rand_list2) #랜덤 값이 입력된 리스트를 zip하기 위해

def my_zip_current(list_1,list_2):#zip할 리스트를 각각 list_1, list_2라 한다.
    zip_list = []
    print('zip 할 리스트:',list_1, ',',  list_2)
    for x, y in zip(list_1, list_2):
        zip_list.append((x, y))

    return zip_list

#b번
def my_unzip():#무작위 리스트 값이 입력 된 1개의 튜플 리스트 생성
    limit_num = random.randint(1,10)
    rand_list = []

    for i in range(limit_num):
        rand_list_tuple = []
        for z in range(2):
            num = random.randint(1, 100)
            rand_list_tuple.append(num)
        rand_list_tuple = tuple(rand_list_tuple)
        rand_list.append(rand_list_tuple)

    return my_unzip_current(rand_list)

def my_unzip_current(list0):#unzip할 튜플로 이루어진 리스트를 list0라 한다. ex)[(1,4),(4,5)]
    unzip_list1= []
    unzip_list2 = []

    print('입력 된 unzip_list:',list0)
    for x in list0:
        unzip_list1.append(x[0])
        unzip_list2.append(x[1])

    return unzip_list1, unzip_list2

if __name__ == '__main__':
    print(my_zip(),'\n')
    result1, result2 = my_unzip()
    print(result1,',',result2)