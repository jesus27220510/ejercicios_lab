import Countriesdata

print("------------a-----------------")
def numero_total_idiomas():
    idiomas = set()  
    
    for country in Countriesdata.countries:
        for language in country['languages']:
            idiomas.add(language)
    
    return len(idiomas)

total_idiomas = numero_total_idiomas()
print("Número total de idiomas en los datos:", total_idiomas)

print("------------------b---------------------")
def diez_idiomas_mas_hablados():
    idiomas = {}
    
    for country in Countriesdata.countries:
        for language in country['languages']:
            if language in idiomas:
                idiomas[language] += country['population']
            else:
                idiomas[language] = country['population']
    
    idiomas_ordenados = sorted(idiomas.items(), key=lambda x: x[1], reverse=True)
    return idiomas_ordenados[:10]

top_idiomas = diez_idiomas_mas_hablados()
print("Diez idiomas más hablados:")
for idioma, poblacion in top_idiomas:
    print(idioma, poblacion)
    
print("----------------------c--------------------")

def diez_paises_mas_poblados():
    paises_ordenados = sorted(Countriesdata.countries, key=lambda x: x['population'], reverse=True)
    return paises_ordenados[:10]

top_paises = diez_paises_mas_poblados()
print("Diez países más poblados:")
for pais in top_paises:
    print(pais['name'], pais['population'])
