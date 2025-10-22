from time import sleep


def f():
    print("jetzt warten")
    sleep(5)
    return "fertig"

def g():
    print("jetzt warten")
    sleep(5)
    yield "fertig"


print("rufe f auf")
e = f()
print("gebe Ergebnis von f aus")
print(e)

print("-" * 30)

print("rufe g auf")
e = g()
print("gebe erstes Ergebnis von g aus")
print(next(e))