msg={"c":2,
"c":2,
"u":3,
"r":2,
"3":2,
"d":2,
"hello":2,
}
x=2
result=0
for k in msg:
    if msg[k]==x:
        result=result+1
print(msg)
print(str(result))
print(msg.get("hello","NOT FOUND "))
print(msg.get("him","NOT FOUND "))

