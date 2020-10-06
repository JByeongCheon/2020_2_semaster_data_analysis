import random

#1번 문제
def estimate_pi(num): #num은 발생시키는 난수의 개수이다.
    count = 0 #원 안에 들어간 횟수
    for i in range(num):
        x = random.random()*2 - 1  #-1 ~ 1 사이의 x와 y값 정의
        y = random.random()*2 - 1
        if (x**2 + y**2) <= 1: #a^2 + b^2 == c^2(피타고라스 정리),제곱이므로 음수의 절대값으로 계산 가능
            count += 1

    return count / num * 4 #test1

if __name__ == '__main__':
    print(estimate_pi(100)) #정수 값 입력
    print(estimate_pi(1000))
    print(estimate_pi(10000))
    print(estimate_pi(100000))


















