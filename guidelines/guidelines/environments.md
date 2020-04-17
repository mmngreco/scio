# Gestión de entornos python

Un entorno virtual es una herramienta que ayuda a mantener separadas las
dependencias requeridas por los diferentes proyectos mediante la creación de
entornos virtuales python aislados para ellos. Esta es una de las herramientas
más importantes que la mayoría de los desarrolladores de Python utilizan.

## ¿Por qué necesitamos un entorno virtual?

Imagina un escenario en el que estás trabajando en dos proyectos python basados
en web y uno de ellos utiliza una `Django 1.9` y el otro utiliza `Django 1.10` y
así sucesivamente. En tales situaciones el entorno virtual puede ser realmente
útil para mantener las dependencias de ambos proyectos.

## ¿Cuándo y dónde utilizar un entorno virtual?

Por defecto, todos los proyectos de su sistema utilizarán estos mismos
directorios para almacenar y recuperar *site packages* (librerías de
terceros). ¿Qué importancia tiene esto? Ahora, en el ejemplo anterior de dos
proyectos, tienes dos versiones de Django. Esto es un verdadero problema para
Python ya que no puede diferenciar entre versiones en el directorio
"site-packages". Así que tanto la `v1.9` como la `v1.10` residirían en el mismo
directorio con el mismo nombre. Aquí es donde entran en juego los entornos
virtuales. Para resolver este problema, sólo tenemos que crear dos entornos
virtuales separados para ambos proyectos, lo mejor de todo es que no hay
límites en el número de entornos que se pueden tener, ya que son sólo
directorios que contienen unos pocos scripts.

El Entorno Virtual debe ser usado siempre que trabaje en cualquier proyecto
basado en Python. Generalmente es bueno tener un nuevo entorno virtual para
cada proyecto basado en Python en el que trabaje. Así que las dependencias de
cada proyecto están aisladas del sistema y entre sí.

## ¿Cómo funciona un entorno virtual?

Hay muchas herramientas para crear entornos aislados de Python. En general
crean una carpeta que contiene todos los ejecutables necesarios para utilizar
los paquetes que un proyecto Python necesitaría.

Fuente: https://www.geeksforgeeks.org/python-virtual-environment/

## Gestores de entornos

Una lista de estas herramientas son, por orden de popularidad:

* [venv](https://docs.python.org/3/library/venv.html)
* [virtualenv](https://virtualenv.pypa.io/en/latest/userguide/#usage)
* [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
* [pipenv](https://pipenv-fork.readthedocs.io/en/latest/install.html#virtualenv-mapping-caveat)
* [poetry](https://poetry.eustace.io/docs/basic-usage/#poetry-and-virtualenvs)


En la documentación de cada uno se encuentra una descripción de como crear un
entorno.

## Un ejemplo usando el módulo built-in de pythton `venv`:

```bash
python -m venv my_project
```

Esto creará una nueva carpeta llamada `my_project` en el actual directorio. Para
activarlo

```bash
source my_project/bin/activate
```

A continución ya estamos listos para poder instalar librerías en el.


## Usando conda


```bash
conda create -n my_project
conda activate my_project
```

