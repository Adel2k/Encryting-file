from cryptography.fernet import Fernet
import sys

if len(sys.argv) == 2:
	filename =  sys.argv[1]

	key = Fernet.generate_key()
	try:
		with open('filekey.key', 'wb') as filekey:
			filekey.write(key)

		with open('filekey.key', 'rb') as filekey:
			key = filekey.read()

		if not key:
			print("The file is empty.")

		fernet = Fernet(key)

		with open(filename, 'rb') as file:
			original = file.read()

		if not original:
			print("The file is empty.")

		encrypted = fernet.encrypt(original)

		with open(f"encrypted-{filename}", 'wb') as encrypted_file:
			encrypted_file.write(encrypted)

	except FileNotFoundError:
		print("File does not exist.")

else:
	print("Please enter the file name to be encrypted")