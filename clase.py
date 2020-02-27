# Autor: Alondra Miranda Aguilera | Alondra Miranda Aguilera
# Descripcion: porcentaje hombres y mujeres

# Escribe tu programa después de esta línea.

mujeres=int(input("Teclea número de mujeres"))
hombres=int(input("Teclea número de hombres"))
inscritos=hombres+mujeres
porcentajeh=(hombres*100)/inscritos
porcentajem=(mujeres*100)/inscritos
print("Mujeres inscritas: ",mujeres)
print("Hombres inscritos: ",hombres)
print("Total de inscritos: ", inscritos)
print("Porcentaje de mujeres: ",porcentajem)
print("Porcentaje de hombres: ",porcentajeh)
