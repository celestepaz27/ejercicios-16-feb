# ============================================
# Nombre: Celeste Paz
# Curso: Programación
# Fecha: 16 de febrero 2026
# Descripción:
# Ejercicios de manipulación de texto y
# procesamiento con SpaCy
# ============================================


# --------------------------------------------
# 1. Crear variable con texto
# --------------------------------------------

texto = "Juan viaja a Colombia el 24 de febrero del año 2026 para comprar 3 computadoras y 2 celulares"

print("Texto original:")
print(texto)
print("-" * 50)


# --------------------------------------------
# 2. Acceder a letras por índice
# --------------------------------------------

print("Primera letra:", texto[0])
print("Cuarta letra:", texto[3])
print("-" * 50)


# --------------------------------------------
# 3. Dividir el texto en palabras
# --------------------------------------------

palabras = texto.split()

print("Lista de palabras:")
print(palabras)
print("Primera palabra:", palabras[0])
print("Segunda palabra:", palabras[1])
print("-" * 50)


# --------------------------------------------
# 4. Dividir usando otro carácter
# --------------------------------------------

division_a = texto.split("a")

print("División usando la letra 'a':")
print(division_a)
print("-" * 50)


# --------------------------------------------
# 5. Procesamiento con SpaCy
# --------------------------------------------

# NOTA:
# Antes de ejecutar este archivo debes instalar:
# pip install spacy
# python -m spacy download es_core_news_sm

import spacy

modelo_idioma = spacy.load("es_core_news_sm")
doc = modelo_idioma(texto)


# --------------------------------------------
# 6. Encontrar nombres de personas
# --------------------------------------------

print("Personas encontradas:")
for entidad in doc.ents:
    if entidad.label_ == "PER":
        print("-", entidad.text)

print("-" * 50)


# --------------------------------------------
# 7. Encontrar lugares o países
# --------------------------------------------

print("Lugares encontrados:")
for entidad in doc.ents:
    if entidad.label_ == "LOC" or entidad.label_ == "GPE":
        print("-", entidad.text)

print("-" * 50)


# --------------------------------------------
# 8. Mostrar todas las entidades detectadas
# --------------------------------------------

print("Todas las entidades detectadas:")
for entidad in doc.ents:
    print(f"{entidad.text} -> {entidad.label_}")
