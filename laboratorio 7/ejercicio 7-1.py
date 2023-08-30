persona = {
 'first_name': 'Edem',
 'last_name': 'Terraza',
 'age': 31,
 'country': 'Peru',
 'is_married': True,
 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
 'address': {
 'street': 'Space street',
 'zipcode': '02210'
 }
}

if 'skills' in persona:
    habilidades = persona['skills']
    cantidad_habilidades = len(habilidades)
    if cantidad_habilidades > 0:
        habilidad_del_medio = habilidades[cantidad_habilidades // 2]
        print(f"Habilidad del medio: {habilidad_del_medio}")
    else:
        print("La lista de habilidades está vacía.")
else:
    print("La persona no tiene habilidades registradas.")
if 'skills' in persona and 'Python' in persona['skills']:
    print("La persona tiene la habilidad 'Python'.")
else:
    print("La persona no tiene la habilidad 'Python'.")
if 'skills' in persona:
    habilidades = persona['skills']
    if set(habilidades) == {'JavaScript', 'React'}:
        print("Él es un desarrollador frontend.")
    elif set(habilidades) == {'Node', 'Python', 'MongoDB'}:
        print("Él es un desarrollador backend.")
    elif set(habilidades) == {'React', 'Node', 'MongoDB'}:
        print("Él es un desarrollador fullstack.")
    else:
        print("Título desconocido.")
else:
    print("La persona no tiene habilidades registradas.")
