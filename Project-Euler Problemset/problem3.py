'''
The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143?
'''

n = 600851475143
factors = []
counter = 3

while(n!=1):
    if(n%counter == 0):
        factors.append(counter)
        n = int(n/counter)
    counter += 1

print("Biggest Prime factor of 600851475143 is :",max(factors))