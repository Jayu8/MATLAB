s1= "abc"
s2= "xyz"
ans = "".join(i for j in zip(s1,s2) for i in j)
#print(ans)




val= ""
for j in zip(s1,s2):
    #print (j)
    for i in j:
         #print (i)
         val += "".join(i)
print(val)


#"".join("".join(i) for i in zip(s1,s2))
