first = {"name":"Sibel Tıpırdamaz","category" : "finance", "experience" : "4 years", "position" : "assistant specialist" }
second = {"name":"Osman Yılmaz","category" : "marketing", "experience" : "10 years", "position" : "coordinator" }
third = {"name":"Melisa Öztürk","category" : "sales", "experience" : "2 years", "position" : "junior" }
fourth = {"name":"Süha Kaya","category" : "research", "experience" : "15 years", "position" : "senior coordinator" }
fifth = {"name":"Toprak Deniz","category" : "human resources", "experience" : "6 years", "position" : "senior specialist" }

all = {}

all[0] = first;
all[1] = second;
all[2] = third;
all[3] = fourth;
all[4] =fifth;

for i in all:
  print(str(i+1)+". CV")
  print("Name: "+ all[i]["name"])
  print("Category: "+ all[i]["category"])
  print("Experience: "+ all[i]["experience"])
  print("Position: "+ all[i]["position"])
  print("*")
