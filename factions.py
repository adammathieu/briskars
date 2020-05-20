from app import db
from app.models import Faction

for faction in ['bannis','celks','ichtiens','maoks','mercenaires','orenauques','quintors','sundars','thuleens']:
    f = Faction(name=faction)
    db.session.add(f)
db.session.commit()
