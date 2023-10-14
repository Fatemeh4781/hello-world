class user:
    def __init__(self, username,password):
     self.username = username
     self.password = password
     
    def printname(self):
        print(self.username , self.password)
        
class buyer(user):
    def __init__(self, username,password,address,codemeli):       
       super().__init__(username,password)
       self.address=address
       self.codemeli=codemeli
       x=buyer("fatemeh123","123","25","2982564789")
       print(x.address)
       print(x.codemeli)