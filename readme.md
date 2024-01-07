# Pilengua, pasos de construcción de una solución.

## 1. Creación del entorno.

- Crear el entorno virtual
```
python -m venv venv
```

- Activar el entorno virtual
```
(win) venv\Scripts\activate
(mac) source venv/bin/activate
```

- Instalar pytest
```
pip install pytest
```

- Guardar las dependencias en requirements.txt (*)
```
pip freeze > requirements.txt
```
(*) Recuerda eliminar las que no sean pytest

- Crear repo git
```
git init
```

## 2. Primer commit con readme y gitflow

- Crear este fichero readme.md
- Crear .gitignore e incluir `venv/` en él.
- Hacer el primer commit

```
git status
git add .
git commit -m "Initial commit"
```