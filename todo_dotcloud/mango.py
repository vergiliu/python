import pymongo

import hashlib
# hashlib.sha256('aaabbbccc').hexdigest()

class MPC():
    def __init__(self):
        connection = Connection('localhost', 27017)
        self.db = connection.users_database
        self.users = self.db.users_collection

    def addUser(self):
        user=raw_input("u:")
        pa=raw_input("p:")
        self.users.insert({'user':user, 'pa':pa})

    def showUsers(self):
        for user in self.users.find():
            print user
           
    def login(self, u, p):
        if self.users.find_one({'user': u}):
            if  self.users.find_one({'user': u, 'pa': p}):
                print "exists"
                self.users.update({'user':u, 'pa':p}, {"$set":{'session':1, 'in': 1}})
            else:
                print "invalid credot"
        else:
            print "not there, adding user"
            gg = self.users.insert({'user':u, 'pa':p})
            print gg

    def logout(self, u, p):
        self.users.update({'user':u, 'pa': p}, {"$set":{'session':None, 'in': 0}})

if __name__ == "__main__":
    u = MPC()
    u.addUser()
    u.showUsers()
   
    us=raw_input("u:")
    p=raw_input("p:")
    u.login(us, p)
    u.showUsers()
    u.logout(us, p)
    u.showUsers()
    
