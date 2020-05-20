# briskars

## db
flask db migrate -m "<comments>"
flask db upgrade

## test db
```
from app import db
from app.models import User, Band
u = User(username='susan', email='susan@example.com')
db.session.add(u)
db.session.commit()
User.query.all()
u = User.query.get(1)
b = Band(name='la bande à garag!', format=500, faction='sundars', author=u)
db.session.add(b)
db.session.commit()
Band.query.all()
```

flask shell
```
flask shell
app
db
```

## start server

```
flask run
```

open http://localhost:5000/

## Issues Encountered

### sqlite3.InterfaceError: Error binding parameter 2 - probably unsupported type. sqlalchemy.exc.InterfaceError: <unprintable InterfaceError object>

With command line, no issue
```
11:36 $ python
Python 3.6.8 (default, Aug  7 2019, 17:28:10) 
[GCC 4.8.5 20150623 (Red Hat 4.8.5-39)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from app import db
[2020-05-20 11:38:04,930] INFO in __init__: briskars band builder startup
>>> from app.models import User, Band
>>> u = User.query.get(2)
>>> u
<User garag2nadrak>
>>> b = Band(name='la bande à garag!', format=500, faction='sundars', author=u)
>>> b
<[sundars][500 PO] la bande à garag!>
>>> db.session.add(b)
>>> db.session.commit()
>>> Band.query.all()
[<[sundars][500 PO] la bande à garag!>]
```

From Flask Form
```
127.0.0.1 - - [20/May/2020 11:46:24] "GET /band HTTP/1.1" 200 -
form.name.data:  test
form.format.data:  300
form.faction.data:  bannis
current_user:  <User garag2nadrak>
<[bannis][300 PO] test>
127.0.0.1 - - [20/May/2020 11:46:26] "POST /band HTTP/1.1" 500 -
Traceback (most recent call last):
  File "/home/maadam/Sources/python/venv/briskars/lib/python3.6/site-packages/sqlalchemy/engine/base.py", line 1284, in _execute_context
    cursor, statement, parameters, context
  File "/home/maadam/Sources/python/venv/briskars/lib/python3.6/site-packages/sqlalchemy/engine/default.py", line 590, in do_execute
    cursor.execute(statement, parameters)
sqlite3.InterfaceError: Error binding parameter 2 - probably unsupported type.

The above exception was the direct cause of the following exception:

...
sqlalchemy.exc.InterfaceError: <unprintable InterfaceError object>
```

Resolution: binding parameter 2 correspond to faction (id is not taken into account)! faction = QuerySelectField(query_factory=lambda: Faction.query.all()) so the type of faction is <class 'app.models.Faction'>, use form.faction.data.name for str.