contacts = {
  ("James",42),
  ("Amy",24),
  ("John",31)
}
name=input()
for x in contacts:
  if name in x:
    print (str (x [0]) , "is", str(x[1]))
    break
  else:
    print("Not Found")