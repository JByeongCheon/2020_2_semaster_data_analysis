import keyword
import operator

#4번
def keyword_count(python_file): #파이썬 파일 지정 ex)text.py
    file = open(python_file, mode = 'r', encoding='UTF-8')
    word  = file.read().split()
    word_counts = dict() #dict선언

    for keyword_word in keyword.kwlist: #keyword.kwlist는  keyword를 리스트로 호출
        word_counts[keyword_word] = word.count(keyword_word)#word문자열에 포함된 keyword의 개수를 딕셔너리 값으로한다.

    word_counts_sort = sorted(word_counts.items(), key=operator.itemgetter(1), reverse = True) #word_counts의 value(값)을 기준으로 역순 정렬

    return word_counts_sort

if __name__ == '__main__':
    print(keyword_count('01_estimate_pi.py')) #파일명 입력