from urllib.request import urlopen

def square(x):
  return x*x

def get_temperature(city):
  url = "https://wttr.in/" + city + "?format=%t"
  page = urlopen(url)
  raw = page.read()
  temp = raw.decode("utf-8")
  return temp

city = input("City : ")
temp = get_temperature(city)
print(temp)
