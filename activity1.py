fav =[]
def add _fav(city):
if len(fav)<3:
  fav.append(city)
  print(city,"added to fav)
        else:
  print("only 3 fav cities allowed:")
def list_fav():
  for city in  fav :
    data = get_ weather(city)
    print(city, data,temp)
  def remove_fav(city):
    if city in fav:
      fav.remove(city)
      print(city, "removed")

while true:
  print("\n1.  search weather)
  print("2. Add fav city)
  print("3. list fav city")
  print("4. remove fav city")
  print("5.exit")

      choice = input("choose option")

            if choice ==1:
              city = input("city name:")
              data = get_weather(city)
              print(data temp)
          elif choice == 2:
              city = input(city name:)
              add_fav(city)
          elif choice==3:
                list_fav()
          elif choice ==4:
                city = input("city name")
                remove_fav(city)
          elif choice ==5:
                break

      
