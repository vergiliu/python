import web
from web import form
from pymongo import Connection
from mongoclass import MongoElements

render = web.template.render('templates/')
urls = (
    '/',        'Index',
    '/login',   'loginScreen',
    '/welcome', 'Welcome',
    '/logout',  'logoutScreen'
)
    
web.config.debug = False
mongoConnection = Connection('localhost', 27017)
databaseTable = mongoConnection.clouds_database
app = web.application(urls, globals())
indexLogin = form.Form(form.Textbox('user'), form.Password('password', form.notnull), form.Button('login/signup'))
my_form = web.form.Form( web.form.Textbox('textfield', id='textfield'), )
session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'uid': None, 'test':'test'})

class Index():
    def GET(self):
        login = indexLogin()
        return render.index(login)

class Welcome:
    def GET(self):
        if session.uid:
            anUser = MongoElements(databaseTable)
            anUser.alreadyLoggedIn(session.uid)
            currentUser = anUser.getMe()
            print "welcome.anuser %s " %  currentUser
            form = my_form()
            return render.tutorial(form, currentUser['userEmail'], currentUser['tasks'])
        else:
            return "use login screen to log in"

    def POST(self):
        form = my_form()
        form.validates()
        s = form['textfield'].value
        print "text was %s" % (s)
        if session.uid:
            anUser = MongoElements(databaseTable)
            anUser.alreadyLoggedIn(session.uid)
            if str(s):
                anUser.addTask(s)
            else:
                print "ceva e in neregula [" +s + "]"
            currentUser = anUser.getMe()
            return render.tutorial(form, currentUser['userEmail'], currentUser['tasks'])
        else:
            return "use login to log in"

class logoutScreen:
    def GET(self):
        #print "uid = %s" % web.ctx.session.uid
        session.uid = None
        session.kill()
        return "you are now logged out, login ? "

class loginScreen:
    def GET(self):
        return "uid % s" % session.uid

    def POST(self):
        loginCredentials = web.input()     # print "user is %s %s" % ( log.user, log.password )
        ongoingLogin = MongoElements(databaseTable)
        anUser = ongoingLogin.login(loginCredentials.user, loginCredentials.password)
        session.uid = anUser
        session.test = 'not test'
        print "session user %s " % session.uid
        if anUser:
            raise web.seeother('/welcome')  #user.login(loginCredentials.user, loginCredentials.password)
        else:
            return "Invalid credentials, please login to continue" #render.index(login)

if __name__ == "__main__":
    web.internalerror = web.debugerror
    app.run()
else:
    web.config.debug = False
    application = app.wsgifunc()
    

