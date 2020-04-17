# Versionado Automático

El versionado automático consiste en enlazar el versionado con los tag del
control de versiones (VCS) de forma que cada vez que queramos sacar una nueva
release, debemos crear un nuevo tag con git.

Para incluir el versionado automático en un proyecto es necesario instalar la
herramienta [`versioneer`](https://github.com/warner/python-versioneer). Esta
herramienta facilita la creación y modificación de los siguientes ficheros:

* `versioneer.py` (nuevo)
* `_version.py` (nuevo)
* `.gitattributes`  (modificación/nuevo)
* `setup.cfg`  (modificación/nuevo)
* `setup.py` (modificación)

## Sobre semantic versioning

El versionado semántico es una estandarización para el reflejar un cambio
importante o necesario en el código, y es el recomendado por el
[`PEP440`](https://www.python.org/dev/peps/pep-0440/#summary-of-permitted-suffixes-and-relative-ordering).

* SemVer :  http://semver.org/
* pros and cons : https://www.geeksforgeeks.org/introduction-semantic-versioning/

![semver](https://bytearcher.com/goodies/semantic-versioning-cheatsheet/wheelbarrel-no-tilde-caret-white-bg-w1000.jpg)


Supongamos un proyecto con la estructura estándar:

```
myprj                (project dir)
├── myprj            (source dir)
│   ├── ...
│   └── __init__.py
├── docs
├── requirements.txt
└── setup.py          (builder)
```

## Instalación de versioneer

El primer paso es instalar el paquete `versioneer` *que luego **no** será una
dependencia* del proyecto.
```
pip install versioneer
```

Una vez tenemos instalada la herramienta, podemos hacer uso de ella. En la
carpeta del proyecto:

```
myprj         (estamos aquí)
├── myprj
│   ├── ...
│   └── __init__.py
├── docs
├── requirements.txt
└── setup.py
```
Se ejecuta el comando que va a modificar y preparar nuestros archivos para el
versionado automático.

```bash
versioneer install
```

Ese comando generará/modificará una serie de ficheros:

* `setup.cfg`     (modificación/nuevo)
* `setup.py`      (modificación)
* `versioneer.py` (nuevo)
* `_version.py`   (nuevo)

## Configurar versioneer

Una vez que se han creado/modificado los archivos pertinentes, tenemos que
terminar de definir el proyecto.

### Editar `setup.cfg`

Hay que decidir los valores que tomarán las siguiente
variables del `setup.cfg`, aquí un ejemplo que puede usarse de template:
```
[versioneer]
VCS = git
estilo = pep440
versionfile_source = myprj/_version.py
versionfile_build = myprj/_version.py
tag_prefix = 
```
Para una explicación más detallada de los parámetros, ver
[aquí](https://github.com/warner/python-versioneer/blob/master/INSTALL.md).

### Editar `setup.py`

Luego tenemos que modificar el `setup.py`, para añadir lo siguiente:

```python
import versioneer
setup(
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    ...)
```

### Lanzar la instalacíon nuevamente

Finalmente, hay que lanzar el comando de instalación de nuevo para dejar todo
cerrado.

```bash
versioneer install
```

## Uso


Versioneer funciona tanto en tiempo de ejecución como en tiempo de instalación. Para más información [ver la
documentación](https://github.com/warner/python-versioneer#theory-of-operation).

Ver la actual version de mi librería:

```bash
$ python -c "import myprj;print(myprj.__version__)"
3.0.5
```

Crear una nueva release:


```bash
$ git tag 3.1.0  # o bien desde la interfaz de gitlab.
$ python -c "import myprj;print(myprj.__version__)"
3.1.0
$ git push && git push --tags # git pull si se hace desde gitlab
```

## Sobre el estilo de los tags (`PEP440`):

Si estamos en el mismo commit del tag veremos:

```bash
$ git checkout 3.0.5
$ git describe
3.0.5
$ pip list | grep myprj
myprj                   3.0.5 /home/user/gitlab/myprj
```

Si estamos a dos commits del tag:

```bash
$ git checkout master
$ git describe
3.0.5
$ pip list | grep myprj
myprj                   3.0.5+2.gb56dcb6 /home/user/gitlab/myprj
```

Si tenemos cambios no commiteados en local:

```bash
$ git describe
3.0.5
$ pip list | grep myprj
myprj                   3.0.5+0.gb56dcb6.dirty /home/user/gitlab/myprj
```

Como se puede ver cada version es perfectamente identificable. El significado
del estilo PEP440 es el siguiente
([link](https://github.com/warner/python-versioneer#styles)):

```
                         3.0.5+0.gb56dcb6.dirty
                         --+-- +  ---+--- --+--
                           |   |     |      |
                           |   |     |      |
tag <----------------------+   |     |      |
commits despues del tag <------+     |      |
commit id <--------------------------+      |
hay cambios no commiteados <----------------+

```
