import requests
import mysql.connector

# Conexión a la base de datos MySQL
connection = mysql.connector.connect(
    host="TU_IP_MySQL",
    user="TU_USUARIO_MySQL",
    password="TU_CONTRASEÑA",
    database="NOMBRE_DE_TU_DB"
)
cursor = connection.cursor()

# Obtener la lista de todos los episodios de la serie
all_episodes = []

for i in range(1, 52):
    # URL de la API
    url = f'https://rickandmortyapi.com/api/episode/{i}'
    r = requests.get(url)
    episode = r.json()
    all_episodes.append(episode)

# Conjunto para almacenar nombres de personajes ya insertados
inserted_characters = set()

# Obtiene nombres, especies y estados de los personajes
for episode in all_episodes:
    characters = episode.get('characters', [])  # Manejo de casos donde no hay personajes
    for character in characters:
        req = requests.get(character)
        js = req.json()
        name = js['name']
        species = js['species']
        status = js['status']
        # Verificar si el personaje ya existe en la base de datos
        cursor.execute("SELECT nombre FROM personajes WHERE nombre = %s", (name,))
        existing_character = cursor.fetchone()
        if existing_character:
            print(f"¡Personaje '{name}' no cargado! Ya existe en la base de datos.")
        elif name not in inserted_characters:
            # Insertar el personaje si no existe en la base de datos
            if species == 'Human':
                species = 'Humano'
            else:
                species = 'Otra'
            if status == 'Alive':
                status = 'Vivo'
            else:
                status = 'Muerto'
            sql_insert = "INSERT INTO personajes (nombre, especie, estado) VALUES (%s, %s, %s)"
            cursor.execute(sql_insert, (name, species, status))
            inserted_characters.add(name)
            print(f"Personaje '{name}' insertado correctamente en la base de datos.")

# Hace un commit para guardar los cambios
connection.commit()

# Cierra la conexión con la base de datos
cursor.close()
connection.close()