#APUNTES DEL CURSO CISCO DE PYTHON

#PARA PRINT 
end="lo que sea" #---> se usa para el final de una cadena, que en vez de saltarse un espacio ponga lo que sea que diga end
sep="-" #---> para que en vez de espacios vaya lo de aqui, ejemplo-asi
print("holi"*3) #---> imprimira holi 3 veces en una misma linea
#\ ---> para poner " o ' en medio de una cadena sin que de error de formato

#LITERALES

print(0o123) #-->Si un número entero esta precedido por un código 0O o 0o (cero-o), el número será tratado como un valor octal. Esto significa que el número debe contener dígitos en el rango del [0..7] únicamente.
print(0x123) #-->es un número hexadecimal con un valor (decimal) igual a 291.

float #--> 4 es un número entero mientras que 4.0 es un número punto-flotante.
print(0.0000000000000000000001) #--->Python siempre elige la presentación más corta del número, E (también se puede utilizar la letra minúscula e - proviene de la palabra exponente)

#booleanos
True and False
/ #--> con este el resultado de la division es un flotante, si pones un numero como 6./4 igual te lo toma como float, pero no resultado especifico, ej:
print(6. // 4)
print (6/4)
#info importante:  el redondeo siempre va hacia abajo.
// # --> mientras que con este es un entero
% #--> El resultado de la operación es el residuo que queda de la división entera.
print(14 % 4)
** #-->  el operador de exponenciación utiliza enlazado del lado derecho.
print(-3 ** 2)
print(-2 ** 3)
print(-(3 ** 2))
