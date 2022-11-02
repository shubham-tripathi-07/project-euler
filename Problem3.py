"""
Problem Statement :

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""


N =   600851475143
answer = 0

for i in range(2,N):
    counter = 0
    for j in range(1,i+1):
        if counter > 2 :break
        if i%j == 0: counter += 1
    if counter == 2:
        while N%i == 0:
            N = N/i
            answer = i           
    if N == 1:break
print(answer)    
