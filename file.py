fname="file.txt"
n=open(fname)
print(n.read())
count=0
a=open("file.txt")

for line in a:
  if line.startswith("x-content:"):
    count=count+1
  print(line)
print(count)