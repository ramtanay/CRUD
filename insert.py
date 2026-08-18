from config import connect

def insert_data(id,name,price,quantity):
  '''
  This function is used to insert data in the db
  '''
  tablename = "products"
  conn = connect()
  cur = conn.cursor()

  sql = f'insert into {tablename} values ({id},"{name}",{price},{quantity})'

  cur.execute(sql)
  conn.commit()
  print("")
  print("-------------------------- Data Inserted Successfully ----------------------------")