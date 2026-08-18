from create_table import new_table
from insert import insert_data 
from fetch import fetch_data
from update import update_data
from delete import delete_data


if __name__=="__main__":
  new_table()

  fetch_data()

  insert_data(1,"Phone",30000,40)
  insert_data(2,"Pendrive",900,32)
  insert_data(3,"Tab",29000,22)
  insert_data(4,"Laptop",90000,82)

  fetch_data()
  update_data("Price",2,1000)
  fetch_data()

  delete_data(3)
  fetch_data()





