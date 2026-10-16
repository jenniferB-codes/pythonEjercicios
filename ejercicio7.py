
#no funciona porque int no puede convertir a entero una string que contenga un numero decimal 
int("3.5")

#Este funciona porque primero el la string que contiene decimal es convertida a un numero decimal y ya luego es convertido a un numero entero
int(float("3.5"))