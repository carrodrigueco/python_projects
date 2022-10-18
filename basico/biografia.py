lst=["nombre completo", "fecha de nacimiento","direccion de residencia","altura","meta(s)"]
dict={}
i=0
while i<len(lst):
    valor=input(f">>> Porfavor ingrese su {lst[i]}...")
    dict[lst[i]]=valor
    i+=1
for i in dict.keys():
    print(">>> "+i.upper()+f": {dict[i]}")