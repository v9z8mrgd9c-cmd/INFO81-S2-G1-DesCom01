# 1. Posiciónate en la carpeta.
cd my-simulation-project/

# 2. Añade el repositorio como un submódulo.
git submodule add https://github.com/REPOREPOREPO.git ppdc-timed-generator

# 3. Inicia y hace update
git submodule init
git submodule update

# 4. Instala la parqueta como un paquete
pip install -e ppdc-timed-generator/

# 5. Hace commit de la referencia a este nuevo sub-módulo
git add .gitmodules ppdc-timed-generator/
git commit -m "Se añadio ppdc-timed-generator como submodulo."