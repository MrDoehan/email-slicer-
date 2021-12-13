game = True
while game == True:
  email = input("Email: ")
  domain = email[email.index("@") + 1:-4]
  name = email[:email.index("@")]
  print(f"Your name is {name} and your domain is {domain}")
  cont = input("Do you want to continue y/n: ")
  if cont == "y":
    game = True
  else:
    game = False  
