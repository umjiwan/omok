# pos

oo = 53
block = 50
running = True
nemo = 0
while running:
    if nemo == 0:
        apb = "a"
    if nemo == 1:
        apb = "b"
    if nemo == 2:
        apb = "c"
    if nemo == 3:
        apb = "d"
    if nemo == 4:
        apb = "e"
    if nemo == 5:
        apb = "f"
    if nemo == 6:
        apb = "g"
    if nemo == 7:
        apb = "h"
    if nemo == 8:
        apb = "i"
    if nemo == 9:
        apb = "j"
    if nemo == 10:
        apb = "k"
    if nemo == 11:
        apb = "l"
    if nemo == 12:
        apb = "n"
    if nemo == 13:
        apb = "m"
    if nemo == 14:
        apb = "o"

    for i in range(15):
        globals()[f"{apb}{i}"] = [oo + (i * 50), (oo + block*(nemo+1))]
        print(globals()[f"{apb}{i}"])
    nemo += 1

    if nemo > 14:
        running = False
    
"""
for i in range(15):
    globals()[f"a{i}"] = [oo + (i * 50), (oo + block*(i+1))] 
for i in range(15):
    globals()[f"b{i}"] = [oo + (i * 50), (oo + block*(i+1))] 
for i in range(15):
    globals()[f"c{i}"] = [oo + (i * 50), (oo + block*(i+1))] 
for i in range(15):
    globals()[f"d{i}"] = [oo + (i * 50), (oo + block*(i+1))] 
for i in range(15):
    globals()[f"e{i}"] = [oo + (i * 50), (oo + block*(i+1))] 
for i in range(15):
    globals()[f"f{i}"] = [oo + (i * 50), (oo + block*(i+1))] 
for i in range(15):
    globals()[f"g{i}"] = [oo + (i * 50), (oo + block*(i+1))] 
for i in range(15):
    globals()[f"h{i}"] = [oo + (i * 50), (oo + block*(i+1))] 
for i in range(15):
    globals()[f"i{i}"] = [oo + (i * 50), (oo + block*(i+1))] 
for i in range(15):
    globals()[f"j{i}"] = [oo + (i * 50), (oo + block*(i+1))] 
for i in range(15):
    globals()[f"k{i}"] = [oo + (i * 50), (oo + block*(i+1))] 
for i in range(15):
    globals()[f"l{i}"] = [oo + (i * 50), (oo + block*(i+1))] 
for i in range(15):
    globals()[f"n{i}"] = [oo + (i * 50), (oo + block*(i+1))] 
for i in range(15):
    globals()[f"m{i}"] = [oo + (i * 50), (oo + block*(i+1))] 
for i in range(15):
    globals()[f"o{i}"] = [oo + (i * 50), (oo + block*(i+1))] 
"""