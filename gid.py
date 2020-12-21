import amino

c=amino.Client()
c.login(email=input("Email: ") ,password=input("Password: "))
print ("By Bovonos")
userlink=input("Type Your Profile Link: ")
user=c.get_from_code(userlink)
userId=user.objectId
comId=user.path[1:user.path.index('/')]
print ("")
print ("")
print ("userId:    ",userId)
print ("comId:      ",comId)