#Explain your work
oddlist = list(range(1,50,2))
evenlist = list(range(0,50,2))
newlist = oddlist + evenlist
newlist = [i*2 for i in newlist]

print (oddlist)
print ("\n")
print (evenlist)
print ("\n")
print (newlist)
print ("\n")
for i in newlist: 
  print (type (i))
