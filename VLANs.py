def verificar_vlan(numero_vlan):
    numero_vlan = int(numero_vlan) 
    
    if 1 <= numero_vlan <= 1000:
        return "La VLAN {} pertenece al rango normal.".format(numero_vlan)
    elif 1001 <= numero_vlan <= 4094:
        return "La VLAN {} pertenece al rango extendido.".format(numero_vlan)
   
numero_vlan = input("Ingrese el número de VLAN: ")

resultado = verificar_vlan(numero_vlan)
print(resultado)