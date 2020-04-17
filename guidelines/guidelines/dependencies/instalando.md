# Instalando Librerías

La **gestión de librerías** es distinto de la **gestión de entornos**, aunque
están relacionados.

La instalación depende del **gestor de librerías** que usemos:

* [pip](https://pip.pypa.io/en/stable/user_guide/)
* [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html#managing-pkgs)
* [pipenv](https://pipenv-fork.readthedocs.io/en/latest/basics.html)
* [otros](https://github.com/topics/packaging)

Es importante saber que la mayoría de herramientas que gestionan librerías
(`pipenv`, `dephell`) delegan en `pip` la gestión de librerías python. Por lo
que en la práctica solo hay dos gestores*:

* [pip](https://pip.pypa.io/en/stable/user_guide/)
* [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html#managing-pkgs)

Nota *: `poetry` es una excepción, no usa `pip` para gesetionar las dependencias.

Tanto `pip` como `conda` pueden trabajar juntos de forma transparente. Podemos
instalar librerías con `pip` o `conda` en el mismo entorno y todo irá bien.
Sin embargo, como regla, está bien usar `pip` como opción preferente.

# Instalación desde varias fuentes

Por defecto, la instalación de una librería se hace buscando un el repositorio
de pip llamado [PyPI](https://pypi.org/) la librería en cuestión. En general a
este tipo de repositorios tienen el nombre de [index](https://pip.pypa.io/en/stable/reference/pip_wheel/#index-url).

```bash
pip install pip-install-test
```

o equivalentemente:

```bash
pip install pip-install-test --index-url https://pypi.org/simple/
```

En este caso el index es el mismo que el de por defecto, pero puede verse
podemos especificar otro distinto.

## desde URL

También podemos instalar desde una url incluyendo delante de la url `git+`,
es decir, `git+url`, por ejemplo:

```bash
pip install git+https://github.com/mmngreco/pkgB
```

## desde Local

Otra forma alternativa es desde nuestro loca, porque o bien hemos creado una
librería nueva, estamos trabajando sobre una existente o hemos clonado el código
fuente, un ejemplo:

```bash
git clone https://github.com/mmngreco/pkgB
cd pkgB
pip install .
```

Dónde `.` significa *ésta carpeta* (es la carpeta donde se encuentra el
`setup.py`). Conseguimos el mismo resultado si hacemos lo siguiente:

```bash
git clone https://github.com/mmngreco/pkgB
pip install ./pkgB
```

# Instalación estática vs dinámica

Otra cuestión a tener en cuenta en la instalación es si queremos una instalación
**estática** o **dinámica** (también se le da el nombre de editable o
desarrollo). La instalación **estática** implica que una copia del código es
copiada en el directorio conocido por Python
[`site-packages`](https://stackoverflow.com/a/46071447/3124367). Por ejemplo:

```bash
git clone https://github.com/mmngreco/pkgB
pip install ./pkgB
```

Esto instala de forma estática `pkgB` en el directorio `site-packages`. Como
consecuencia si estamos trabajando sobre el proyecto `pkgB` en local, y hacemos
cambios sobre el código, por ejemplo incluimos una nueva función. Con el
procedimiento de instalación descrito hasta ahora, si hacemos `import pkgB` en
python el código de `pkgB` será el antiguo y por tanto no tedrá esa nueva función.
Si queremos usar el nuevo código tendremos que hacer nuevamente:

```bash
pip install ./pkgB
```

Esto puede resultar molesto en algunas ocaciones, para ello existe la
posibilidad de instalar de forma **dinámica** una librería:

```bash
pip install --editable ./pkgB
```

o equivalentemente:

```bash
pip install -e ./pkgB
```

Con la instalación dinámica conseguimos que cada vez que iniciemos Python
tengamos la última versión al hacer `import pkgB`.

# Recursos:

* https://realpython.com/what-is-pip/
* https://www.anaconda.com/understanding-conda-and-pip/
