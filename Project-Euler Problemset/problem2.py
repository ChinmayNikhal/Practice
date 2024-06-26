'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 
1 and 2, the first terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the 
sum of the even-valued terms.
'''

esum = 0
fibo = [1,2]
given_limit = 4000000
while(fibo[1] < given_limit):
    check = fibo[0] + fibo[1]
    if(fibo[1]%2 == 0):
        esum += fibo[1]
    fibo.pop(0)
    fibo.append(check)

print('Even Sum is',esum)