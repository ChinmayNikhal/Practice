'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 
2-digit numbers is 9009=91x99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

biggest = 0
counter_a = 999

while(counter_a >= 100):
    counter_b = 999
    while(counter_b >= 100):
        temp = counter_a * counter_b
        if(str(temp) == (str(temp))[::-1]):
            if(biggest < temp):
                biggest = temp

        counter_b -= 1
    counter_a -= 1

print(biggest)