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
print(aa is a()) # como resultado aparece por pantalla "False"
z = aa.y 
print(z(())) # como resultado aparece por pantalla "0"
print(a().y((a,))) #  como resultado aparece por pantalla "1"
print(A.y(aa, (a,z))) # como resultado aparece por pantalla "2"
print(aa.y((z,1,'z'))) # como resultado aparece por pantalla "3"
```
