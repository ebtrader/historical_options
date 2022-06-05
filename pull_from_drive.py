with open('host.txt') as g:
    hostname = g.read()

with open('dbname.txt') as f:
    var = f.read()

with open('username.txt') as h:
    username = h.read()

with open('pwd.txt') as i:
    pwd = i.read()

application = Flask(__name__)

application.config['MYSQL_HOST'] = hostname
application.config['MYSQL_USER'] = username
application.config['MYSQL_PASSWORD'] = pwd
application.config['MYSQL_DB'] = var