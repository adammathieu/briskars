# briskars

## db
flask db migrate -m "<comments>"
flask db upgrade

## test db
```
from app import db
from app.models import User, List
u = User(username='susan', email='susan@example.com')
db.session.add(u)
db.session.commit()
User.query.all()
u = User.query.get(1)
l = Post(name='la bande de susan!', author=u)
db.session.add(l)
db.session.commit()m
List.query.all()
```

flask shell
```
flask shell
app
db
```