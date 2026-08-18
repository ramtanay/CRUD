from config import connect

def fetch_data():
  '''
  This function is used to fetch data from the db
  '''
  tablename = "products"
  conn = connect()
  cur = conn.cursor()
  sql = f"select * from {tablename};"

  cur.execute(sql)

  result =  cur.fetchall()

  i = 0

  for _ in result:
    print(_)
    i+=1
  print("")
  print(f"------------------------- {i} Record Retrived Successfully ------------------------------")