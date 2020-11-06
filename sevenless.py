#How to use range to get numbers from 0-99
print(list(range(100)))


#First I made a range that counts by 7
problem1 = list(range(100))

for i in problem1:
    if (i%7==0):
        print(i)
        
        
#Then I made the opposite (a sevenless range)
for i in problem1:
    if (i%7!=0):
        print(i)