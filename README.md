# ejercicios_de_parejas

Enlace de este repositorio: https://github.com/acasasaez/ejercicios_de_parejas/edit/main/README.md




Ejercicio 3:
```
class A:
def z(self): 
        return self 
 
    def y(self, t): 
        return len(t) 
 
a = A 
y = a.z 
print(y(a)) #?????
aa = a() 
print(aa is a()) #False
z = aa.y 
print(z(())) #0
print(a().y((a,))) #1 
print(A.y(aa, (a,z))) #2
print(aa.y((z,1,'z'))) #3
```
