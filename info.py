user_info = {
	"first_name" : "Andrey",
	"last_name" : "Degozhskiy"
}
print(user_info["last_name"])

f_name = input("Enter you first name:\n").capitalize()
user_info['first_name'] = f_name

l_name = input("Enter you last name:\n").capitalize()
user_info['last_name'] = l_name

print(user_info)