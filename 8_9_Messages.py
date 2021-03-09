# 8-9. Messages: Make a list containing a series of 
# short text messages. Pass the list to a function 
# called show_messages(), which prints each text 
# message.

lista = ["Hola", "Hallo", "Salut", "hello"]

def show_messages(lista):
	"""Printing every message in the list"""
	for message in lista:
		print(message)

show_messages(lista)