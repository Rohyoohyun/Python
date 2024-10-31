import random 
import time

wlist = ['cat','dog','fog','monkey','mouse','panda','frog','snake','wolf'] #리스트의 단어는 자신이 원하는 것으로 변경해봅시다. 문장도 가능합니다.
print('[타자게임]준비되면 엔터!') 
input() # 사용자가 엔터를 누를 때까지 기다림

start = time.time() # 시작 시간을 기록

com = random.choice(wlist) 
n = 1
while n <= 5 :
    print(com) 
    player=input()
    if player == com: # 문제와 입력이 같을 때
        print('통과!') # "통과!"출력
        n += 1 # 문제 번호 1 증가
        random.choice(wlist)# 새 문제 뽑기
    else:
        print('오타! 다시 도전!')
    end = time.time()
    wt = end - start
    print(f'타자 시간 : {wt:.2f} 초')