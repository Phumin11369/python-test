#type conversion

A=1
B=2.1
C="20"
#แปลง1บรรทัด
result = A+B
print(result)
result2 = A+int(C) #แปลงC เป็นint
print(result2)
result3 = str(A)+C #แปลงA เป็นstr
print(result3)
print(float(C))
print(str(B))

#แปลงถาวร
C=float(C)
print(type(C))
print(C)
