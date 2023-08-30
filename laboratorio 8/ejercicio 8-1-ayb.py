import sys
import os

# Obtener la ruta completa del directorio actual
current_directory = os.path.dirname(os.path.abspath(__file__))

# Agregar la ruta al sys.path
sys.path.append(current_directory)

# Ahora puedes importar módulos desde este directorio
import countriesdata

# Luego puedes usar las funciones definidas en el módulo countries_data
