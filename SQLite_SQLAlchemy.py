import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

conn = sa.create_engine('sqlite://')

def drop_table_zoo(conn):
    conn.execute('''drop table zoo''')
    print 'table zoo dropped.'
    print '-' * 100

conn.execute('''create table zoo 
(critter varchar(20) primary key,
count int , 
damages float)''')

ins = 'insert into zoo(critter, count, damages) values(?, ?, ?)'
conn.execute(ins, ('duck', 10, 0.0))
conn.execute(ins,'bear', 2, 1000.0)
conn.execute(ins,'weasel', 1, 2000.0)
inserts = list()

rows = conn.execute('select * from zoo')
print(rows)
for row in rows:
    print row
    inserts.append(row)

# print inserts
drop_table_zoo(conn)

print 'creating table and inserting rows using SQL expression language..'
meta = sa.MetaData()
zoo = sa.Table('zoo', meta, \
        sa.Column('critter', sa.String, primary_key=True),\
        sa.Column('count', sa.Integer),\
        sa.Column('damages', sa.Float)\
        )
meta.create_all(conn)
print 'table zoo created..'
for i in inserts:
    conn.execute(zoo.insert(i))

result = conn.execute(zoo.select())
for i in result.fetchall():
    print i

print '-'*100

drop_table_zoo(conn)

conn = sa.create_engine('sqlite:///zoo.db')

Base = declarative_base()
class Zoo(Base):
    __tablename__ = 'zoo2'
    critter = sa.Column('critter', sa.String, primary_key=True)
    count = sa.Column('count', sa.Integer)
    damages = sa.Column('damages', sa.Float)
    def __init__(self, critter, count, damages):
        self.critter = critter
        self.count = count
        self.damages = damages
    def __repr__(self):
        return  "<Zoo({}, {}, {})>".format(self.critter, self.count, self.damages)

Base.metadata.create_all(conn)

first = Zoo('duck', 10, 0.0)
second = Zoo('bear',2,1000.0)
third = Zoo('weasel', 1, 2000.0)
fourth = Zoo('duck', 1, 1.0)

Session = sessionmaker(bind=conn)
session = Session()

session.add(first)
session.add_all([second, third])
session.add(fourth)
try:
    session.commit()
except Exception as e:
    print e.message, e.args

