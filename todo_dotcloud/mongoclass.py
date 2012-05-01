import pymongo
import hashlib

#user = {"email": "aaa@bbb.ccc", "pass": "abc"}
#users.find_one()
#users.insert(user)

class MongoElements():
    def __init__(self, mongoDatabase):
        self.users = mongoDatabase.users_collection #tables
        self.loggedUser = None
        # login or signup

    def login(self, useremail, userpass):
        hashOfPass = hashlib.sha256(userpass).hexdigest()
        if self.users.find_one({'userEmail': useremail}):
            myLoggedUser = self.users.find_one({'userEmail': useremail, 'userPass': hashOfPass})
            if myLoggedUser:
                print "User exists, will log in"
                self.users.update({'userEmail': useremail, 'userPass': hashOfPass}, {"$set":{'session': 1, 'isLogged': True}})
                self.loggedUser = myLoggedUser['_id']
            else:
                return None # "invalid credentials"
        else:
            print "User not present, adding user"
            self.loggedUser = self.users.insert({'userEmail': useremail, 'userPass': hashOfPass, 'tasks': {}})
            print "created new user ", useremail
        return self.loggedUser

    def alreadyLoggedIn(self, uid):
        print "uid %s" % uid
        self.loggedUser = uid

    def logout(self):
        self.users.update({'_id': self.loggedUser}, {"$set":{'session': None, 'isLogged': False}})

    def displayAll(self):
        for user in self.users.find():
            print user
    
    def cleanDatabase(self):
        for user in self.users.find():
            self.users.remove(user)
        print "mongo table is cleaned"

    def addTask_RI(self):
        noteDescription = raw_input('descr:')
        tasks = self.users.find_one({'_id': self.loggedUser})['tasks']
        if not tasks: tasks = {}
        tasks[noteDescription] = []
        self.users.update({'_id': self.loggedUser}, {"$set": {'tasks': tasks}})

    def addTask(self, description):
        description.replace(" ", "_")
        tasks = self.users.find_one({'_id': self.loggedUser})['tasks']
        if not tasks: tasks = {}
        tasks[description] = []
        self.users.update({'_id': self.loggedUser}, {"$set": {'tasks': tasks}})

    def searchOne(self, emailAddress):
        if self.loggedUser:
            return self.users.find_one({"_uid": self.loggedUser})
        else:
            return self.users.find_one({"userEmail": emailAddress})

    def getMe(self):
        return self.users.find_one({'_id': self.loggedUser})

if __name__== "__main__":
    mongoConnection = pymongo.Connection('localhost', 27017)
    databaseTable = mongoConnection.clouds_database
    m = MongoElements(databaseTable)
#    m.cleanDatabase() ## drop :)
    m.displayAll()
    userEmail = raw_input("userEmail:")
    userPass = raw_input("userPass:")
    m.login(userEmail, userPass)
    m.addTask_RI()
    m.displayAll()
    m.logout()

