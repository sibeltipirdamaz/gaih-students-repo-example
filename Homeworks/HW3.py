num=0
d = {}
list = [0.0,0.0,0.0,0.0,0.0]
while num<5 : 
  name = input ("Enter your name ")
  midterm = int(input("What is your midterm grade? "))
  project = int(input("What is your project grade? "))
  final =  int(input("What is your final grade? "))  
  passingGrade = midterm*0.3 + project*0.3 + final*0.4
  d[name] = passingGrade
  list[num] = passingGrade
  num=num+1

print(list)
list.sort()
list.reverse()
print(list)
