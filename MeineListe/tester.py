import meineliste

liste_meine = meineliste.Liste()

liste_python = list()

# print(liste_meine)
# print(liste_python)

# if str(liste_meine) != str(liste_python):
#     print("Alarm, es ist NICHT gleich!")
# --> zusammengefasst in Zeile 14

assert str(liste_meine) == str(liste_python), "Alarm, es ist NICHT gleich!"
print('---OK!---')

assert len(liste_meine) == len(liste_python), "leere Listen nicht gleich lang"


liste_python.append(1)
liste_meine.append(1)
assert len(liste_meine) == len(liste_python), "nicht gleich lang"
print(len(liste_meine))
# for i in range(10):
#     liste_meine.append(i)
#     print(len(liste_meine))