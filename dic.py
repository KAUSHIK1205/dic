student={
"id":{"k" :"Kaushik", "rollno":12},
"id3":{"k" :"codingal", "rollno":10},
"id21":{"k" :"raspberrypipico", "rollno":1},
"id123":{"k":"aurdino uno r3","rollno":7},
"id1234":{"k":"raspberrypipico","rollno":1}
}
result={}
for k,v in student.items():
    if v not in result.values():
        result[k]=v
    
print(result)
