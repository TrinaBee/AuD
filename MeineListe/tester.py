from meineliste_iterativ import Liste as ListeI
from meineliste_rekusiv import Liste as ListeR

liste_meine_i = ListeI()
liste_meine_r = ListeR()

liste_python = list()

print(liste_meine_i)
print(liste_meine_r)
print(liste_python)

if str(liste_meine_i) != str(liste_python):
    print("Alarm, es ist NICHT gleich!")


assert str(liste_meine_i) == str(liste_python), "Alarm, es ist NICHT gleich!"
assert str(liste_meine_r) == str(liste_python), "Alarm, es ist NICHT gleich!"
print('---OK!---')

assert len(liste_meine_i) == len(liste_python), "leere Listen nicht gleich lang"
assert len(liste_meine_r) == len(liste_python), "leere Listen nicht gleich lang"


liste_python.append(1)
liste_meine_i.append(1)
liste_meine_r.append(1)
assert len(liste_meine_i) == len(liste_python), "nicht gleich lang"
assert len(liste_meine_r) == len(liste_python), "nicht gleich lang"

for i in range(4):
    liste_python.append(i)
    liste_meine_i.append(i)
    liste_meine_r.append(i)

# for elem in [1,"str",True,0.1,]:
#     liste_python.append(elem)
#     liste_meine_i.append(elem)
#     liste_meine_r.append(elem)
print('----------Länge(py,i,r)----------')
print(len(liste_python))
print(len(liste_meine_i))
print(len(liste_meine_r))

print('----------Listen(i,r)----------')
print(liste_meine_i)
print(liste_meine_r)

kopie_liste_i = liste_meine_i.copy()
kopie_liste_r = liste_meine_r.copy()
print('----------Kopie(i,r)----------')
print(kopie_liste_i)
print(kopie_liste_r)


print(liste_meine_i[4])
print(liste_meine_r[4])

# for elem in liste_meine_i:
#     print(elem)
print('----------Unique1 i)----------')
print(kopie_liste_i)
unique1 = kopie_liste_i.unique1()
print(unique1)
print('----------Unique2 i)----------')
print(kopie_liste_i)
unique2 = kopie_liste_i.unique2()
print(unique2)
print('----------Unique r)----------')
print(kopie_liste_r)
unique = kopie_liste_r.unique()
print(unique)