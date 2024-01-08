# Silabeador

## 1. Crear la feature con git flow

```
git flow feature start silabeador
```

## 2. Primeros tests

- Buscar grupos de vocales
- Añadir la consonante de la izquierda
- Agregar sobrantes a la derecha
- caso y como vocal y consonante
- caso especial *in*

Para cada caso se hace un test y una vez se pasa se hace un commit indicando el test superado, así en el histórico de commits se ve el desarrollo del producto.

### 2.1 Grupos vocalicos basicos.

- Recuerda crear el fichero `__init__.py` en la carpeta tests para que funcione la importacion de `silabeador.py` en los tests

- Al hacer el commit veo que se han creado carpetas `__pycache__` y `.vscode`. Las incorporo al `.gitignore`.

### 2.2 Grupos de dos o mas vocales seguidas. Posibles diptongos.
- Se cambia la solución sencilla del filter a un bucle en que se van añadiendo vocales a cada grupo. No se comprueban sus relaciones (es decir si son diptongos o hiatos, ver [requisitos](requisitos.pdf))

### 2.3 Grupos de dos o mas vocales seguidas con reglas de hiato.
- Un hiato se produce cuando se dan dos vocales abiertas consecutivas (se separan las vocales en grupos distintos).
- En `cafeína`, la `í` es abierta y la `e` también.
- En `salíais`, la primera `í` y la `a` son abiertas, se separan, sin embargo como la segunda `i` es cerrada, permanece unida a la a y se separan en `í`, `ai`

### 2.4 Trabajo con mayusculas
- Debe seguir funcionando independientemente de si las palabras estan escritas en mayuscula o minuscula y mantener el tipo original

### 2.5 Localizar la constante o grupo de constantes a la izquierda del grupo vocalico.
- Usaremos la palabra `compruebo`, la primera silaba es facil solo tiene una `c`, la segunda tiene `pr` pero no debe incluir la `m` y la tercera vuelve a ser sencilla. 
- Es posible que para poder cruzar los grupos de vocales con el resto de la palabra nos interese meter la posicion del grupo en la palabra, afectando a todos los tests anteriores.
- Y lo mejor es, entonces, devolver tuplas, tal que `(posicion: int, grupo: str)`. Lo haré con namedTuples