"""Tuplas: son estructuras de datos similares a las listas.
 - Son inmutables. 
 - Se crean con ()
 - Son una secuencia de elementos
 - Usualmente se usan para contraseñas, al caracterizarse por ser inmutables"""

tupla=(1,2,3,"k","queso","c");
print(tupla);
print(type(tupla));


"""Modificar un elemento: NO SE PUEDE 
#tupla[1]=100; ---> daria error porque las tuplas son inmutables"""

#Diferentes maneras de crear tuplas
tupla1=(1,2,3);
tupla2=1,2,3;
tupla3=tuple([1,2,3,4]); #---> se convierte una LISTA en TUPLA usando tuple
print(type(tupla3)); 

#Acceder a un elemento dentro de una tupla
