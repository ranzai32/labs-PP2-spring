class Parrot:

    # атрибуты класса
    species = "птица"

    # атрибуты экземпляра
    def __init__(self, name, age):
        self.name = name
        self.age = age

# создаем экземпляра класса
kesha = Parrot("Кеша", 10)
cookie = Parrot("Куки", 15)

# получаем доступ к атрибутам класса
print("Кеша — {}".format(kesha.__class__.species))
print("Куки тоже {}".format(cookie.__class__.species))

# получаем доступ к атрибутам экземпляра
print("{} — {}-летний попугай".format(kesha.name, kesha.age))
print("{} — {} летний попугай".format(cookie.name, cookie.age))