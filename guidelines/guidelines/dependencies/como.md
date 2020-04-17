# ¿Cómo especificar una dependencia (privada)?

Suponemos que hemos desarrollado una librería llamada `my_pkg`. Esta librería
usa `prj` `numpy`, por tanto, ambas son una dependencia de `my_pkg`. En este
caso necesitamos incluir `numpy` en los archivos `setup.py` y en el
`requirement.txt` de nuestro proyecto.

## Escribiendo un archivo `setup.py`

Dado que la dependencias que vamos a incluir es privada debemos incluir
de información de la fuente de la cuál descargara la dependencia. Esto no es
necesario cuando las dependencias están en `PyPi`.
En nuestro caso, el `setup.py` debería tener el siguiente aspecto:

```python
from setuptools import setup


setup(
    ...
    install_requires=[
        'prj VERSION_SPECIFIER',
    ],
    dependency_links=[
        'http://server/grp/prj.git@TAG_NAME#egg=prj-VERSION'
    ],
)
```

Dónde:

- `VERSION_SPECIFIER` denota la versión mínima, máxima o exacta* que este
  proyecto requiere. Para más información ver el
  [`PEP440`](https://www.python.org/dev/peps/pep-0440/).
- `TAG_NAME` es el tag, rama o commit del VCS que va a ser descargado.
- `VERSION` es la versión exacta a la que `dependency links` está referenciando.
  El proceso de instalación comprobará si esta versión es coherente con
  `VERSION_SPECIFIER`. Aunque la versiones no importen hay que escribir algo.
  Poner `VERSION` igual `0` es una buena opción para esto.


Por último pero no menos importante, si queremos que el proceso de instalación
procese la sección `dependency_links` es necesario incluir el modificador
`--process-dependency-links` al comando de instalación.


```bash
$ pip install --process-dependency-links my_pkg
```

> El modificador `--process-dependency-links` está deprecado, y ha desaparecido
> a partir de la versión 19 de pip.
> [Ver link](https://github.com/pypa/pip/issues/6162) para mas información.

## Escribiendo un `requirements.txt`

Es muy importante tener clara la diferencia entre `setup.py` y
`requirements.txt`.

Todo paquete instalable necesita tener un `setup.py` para tener un proceso
de instalación (se puede hacer `pip install`) por el contrario `requiremets.txt`
es opcional.

No obstante, cuando su paquete va a ser utilizado en una prueba o producción
es conveniente incluir un archivo `requirements.txt` que especifique
todas las dependencias necesarias para configurar correctamente el entorno
(de hecho, algunos de sus colegas pueden pedirle que incluya un archivo
`requirements.txt` para que ellos puedan ser capaz de reproducir el mismo
entorno que usted tiene). Además, para evitar sorpresas no deseadas, las
dependencias en un archivo `requirements.txt` deben ser especificado usando
números de versiones exactas (usando `==`).

Veamos un candidato de `requirement.txt` que acompaña al `setup.py` de arriba.

```
--process-dependency-links
numpy==1.13.1
pandas==0.21.3
http://server/grp/prj.git@TAG_NAME#egg=prj-VERSION
...
```

Notar que hemos pasado `--process-dependency-links` dentro del `requirements.txt`.
Esto nos permite excluirlo del comando de instalación, asi pues podemo ejecutar:

```bash
pip install my_pkg -r requirements.txt
```

en lugar de:

```bash
pip install my_pkg -r requirements.txt --process-dependency-links
```

### ¿Qué contiene un `requirements.txt`?

El `requirement.txt` contiene **todas** las dependencias concretas que definen un
entorno de ejecución. Esto es, las dependencias de primer nivel y además las
sucesivas dependencias de éstas.

En el `requirement.txt` nos interesa fijar todo: pensar por ejemplo que dejamos
una dependencia fuera (no la recojemos en el requirement), si esta librería
cambia radicalemente (suben la version por que usan una nueva api) nuestro
proyecto, en el siguiente despliegue fallará.

Lo que querremos es minimizar estas situaciones y que nuestro proyecto siga
funcionando. Para asegurar el buen despliegue, debemos incluír todas las
dependencias, de lo contrario, con el paso del tiempo será mas probable que
una dependencia cambie lo suficiente como para que nuestro proyecto deje de
funcionar correctamente.

### Un workflow para generar

1. Crear un nuevo entorno
1. Desplegar el proyecto con las dependencias básicas (`pip install .` o
   `pip install -r requirements-base.txt`).
1. Testear el correcto funcionamiento
1. Congelar versiones (`pip freeze > requirements.txt`)
1. Crear un nuevo entorno
1. Deplegar el proyecto con el requirement-file
1. Testear el correcto funcionamiento

Harramientas que pueden facilitar este trabajo:

1. [Docker](https://www.docker.com/get-started)
1. [tox](https://tox.readthedocs.io/en/latest/)
1. [tox-conda](https://github.com/tox-dev/tox-conda)
1. [tox-docker](https://github.com/tox-dev/tox-docker)


