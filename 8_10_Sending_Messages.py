# 8-10. Sending Messages: Start with a copy of your 
# program from Exercise 8-9. Write a function called 
# send_messages() that prints each text message and 
# ves each message to a new list called sent_messages
#  as it’s printed. After calling the function, 
#  print both of your lists to make sure the 
#  messages were moved correctly.

messages = ["Hola", "Hallo", "Salut", "hello"]
sent_messages = []

def send_messages(messages, sent_messages):
	""" Printing messages"""
	while messages:
		current_message = messages.pop()
		print(current_message)
		sent_messages.append(current_message)

send_messages(messages, sent_messages)

print("Printing each sent message")
for x in sent_messages: 
	print(x)

print("Printing message list")
print(messages)

		