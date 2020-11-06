#How to use range to get numbers from 0-99
print("This is a range from 0-99")
print(list(range(100)))
print("-----")


#First I made a range that counts by 7
problem1 = list(range(100))
print("This range counts by 7")

for i in problem1:
    if (i%7==0):
        print(i)
        
print("-----")
        
        
#Then I made the opposite (a sevenless range)
print("This range is sevenless")
for i in problem1:
    if (i%7!=0):
        print(i)
print("-----")