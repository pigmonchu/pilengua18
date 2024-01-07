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
