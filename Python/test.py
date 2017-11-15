def no_of_holes(str):
    hole1 = ['0','4','6','9']
    hole2 = '8'
    count=0
    count+=val for hole in hole1 if(val=str.count(hole))>0
    return count


no_of_holes("12345678")
# test_cases = int(input())
# for i in range(0, test_cases):
#     test = input()
#     print (no_of_holes(test))    


# def holes(str):
#     hole1 = ['0','4','6','9','8']
#     hole2 = '8'
#     found=0
#     for hole in hole1:
#         if str.count(hole)>0:
#             if hole == hole2:
#                     found+=str.count('8')*2
#             else:
#                 found+=str.count(hole)
#     return found
#
# amount = input()
# for i in range(0, amount):
#     test = raw_input()
#     print holes(test)
#
# #ans = holes("1233445235308968")
# #print(ans)
