guest_list = ["Tesla", "Turing", "Hamilton"]
print(f"La lista de invitados es {guest_list[0]}, {guest_list[1]} y {guest_list[2]}.")

print(f"Desafortunadamente {guest_list[0]} no podra venir a  la fiesta")

# Eliminando Tesla de la lista
del guest_list[0]
print(guest_list)	
 
# Agregando a Amelia
guest_list.insert(0, "Amelia")
print(guest_list)

# Print call
print(f"We found a bigger table so there will me more people coming")

# Agregando a 3 mas invitados
guest_list.insert(0, "Einstein")
guest_list.insert(2, "Marie Curie")
guest_list.append("Ada Lovelance")

print(guest_list)

for element in guest_list:
	print(f"Invitacion a {element}")

print(f"Unfortunely the table isn't comming on time so, only two people will come")	


print(f"Sorry for des-invite you {guest_list.pop()}")
print(f"Sorry for des-invite you {guest_list.pop()}")
print(f"Sorry for des-invite you {guest_list.pop()}")
print(f"Sorry for des-invite you {guest_list.pop()}")

print(f"You can still come {guest_list[0]}")
print(f"You can still come {guest_list[1]}")

print(guest_list)

del guest_list[1]
del guest_list[0]
print(guest_list)