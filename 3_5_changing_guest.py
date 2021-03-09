guest_list = ["Tesla", "Turing", "Hamilton"]
print(f"La lista de invitados es {guest_list[0]}, {guest_list[1]} y {guest_list[2]}.")

print(f"Desafortunadamente {guest_list[0]} no podra venir a  la fiesta")

# Eliminando Tesla de la lista
del guest_list[0]
print(guest_list)	
 
# Agregando a Amelia
guest_list.insert(0, "Amelia")
print(guest_list)