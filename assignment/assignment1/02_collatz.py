import random

#2번 문제
def collatz():
    collatz_list = [ ]
    num = random.randint(1,100) #num은 무작위의 정수 x이다.
    print('입력 값:',num)

    while num != 1:
        num = num * 3 + 1 if num % 2 else num // 2
        collatz_list.append(num)

    return collatz_list

if __name__ == '__main__':
    print(collatz())
