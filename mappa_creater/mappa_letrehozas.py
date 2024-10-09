import os

# A fájl elérési útja (nevezzük "mappak.txt"-nek, és helyezd ugyanabba a mappába, mint a Python script)
file_path = 'mappak.txt'

# Az aktuális munkakönyvtár lekérése (ahol a script fut)
base_directory = os.getcwd()

# A fájl megnyitása és a mappanevek beolvasása
with open(file_path, 'r', encoding='utf-8') as f:
    for line in f:
        folder_name = line.strip()  # Eltávolítja a sortörést és egyéb felesleges karaktereket
        if folder_name:  # Csak akkor hozzon létre mappát, ha a név nem üres
            folder_path = os.path.join(base_directory, folder_name)
            os.makedirs(folder_path, exist_ok=True)  # Mappa létrehozása, ha nem létezik

print(f"Mappák sikeresen létrehozva a következő helyen: {base_directory}")
