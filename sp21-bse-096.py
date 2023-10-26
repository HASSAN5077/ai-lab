x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)

x = 5
y = "John"
print(type(x))
print(type(y))

x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x)
print(y)
print(z)
print(w)

a = "Hello"
print(a)
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

a = "Hello"
b = "World"
c = a + b
print(c)

thislist = ["apple", "banana", "cherry"]
print(thislist)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

thisset = {"apple", "banana", "cherry"}
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(len(thisset))

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


  i = 1
while i < 6:
  print(i)
  i += 1

  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

    def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")