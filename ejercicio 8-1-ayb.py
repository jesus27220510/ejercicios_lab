import Countriesdata

def idiomas_mas_hablados():
    idiomas = {}
    
    for country in Countriesdata.countries: 
        for language in country['languages']:
            if language in idiomas:
                idiomas[language] += country['population']
            else:
                idiomas[language] = country['population']
    
    idiomas_ordenados = sorted(idiomas.items(), key=lambda x: x[1], reverse=True)
    return idiomas_ordenados[:10] 

print("--------------a-------------")
top_idiomas = idiomas_mas_hablados()
print(top_idiomas)

print("--------------b-------------")
def paises_mas_poblados():
    paises_ordenados = sorted(Countriesdata.countries, key=lambda x: x['population'], reverse=True)
    return paises_ordenados[:10] 

top_paises = paises_mas_poblados()
print("\nLos países más poblados:")
for pais in top_paises:
    print(pais['name'], pais['population'])
