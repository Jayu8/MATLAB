def no_of_holes(str):
    hole1 = ['0','4','6','9']
    hole2 = '8'
    count=0
    for hole in hole1:
        if str.count(hole)>0:
            count+=str.count(hole)
    if str.count(hole2)>0:
        count+=str.count(hole2)*2
    return count

test_cases = int(input())
for i in range(0, test_cases):
    test = input()
    print (no_of_holes(test))
