# 8-11. Archived Messages: Start with your work 
# from Exercise 8-10. Call the function send_messages() 
# with a copy of the list of messages. After calling 
# the function, print both of your lists to show that 
# he original list has retained its messages.

messages = ["Hola", "Hallo", "Salut", "hello"]
sent_messages = []


def send_messages(messages, sent_messages):
	""" Printing messages"""
	while messages:
		current_message = messages.pop()
		print(current_message)
		sent_messages.append(current_message)

send_messages(messages[:], sent_messages)

print("Printing each sent message")
for x in sent_messages: 
	print(x)

print("Printing message list")
print(messages)
