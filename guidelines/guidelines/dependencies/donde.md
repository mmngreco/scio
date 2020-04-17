# ¿Dónde se definen las dependencias?

Para poder distribuir (compartir) correctamente nuestro proyecto tenemos que
definir correctamente nuestras dependencias. Para esto, hay que prestar
atención a dos ficheros dentro de nuestra
[estructura de proyecto](https://docs.python-guide.org/writing/structure/).

Si el proyecto que estamos desarrollando es instalable (existen proyectos no
instalables) entonces tendremos un `setup.py` en nuestro directorio raíz y
además un `requirements.txt`.


* [`setup.py`](https://stackoverflow.com/questions/1471994/what-is-setup-py) (solo instalables)
* [`requirements.txt`](https://pip.pypa.io/en/stable/user_guide/#requirements-files) (opcional)

> [Diferencias entre `setup.py` y `requirements.txt`](https://caremad.io/posts/2013/07/setup-vs-requirement/)


Existen dos tipos principales de proyectos:

## Librerías

* Son instalables (se distribuye).
* están pensadas pensadas para ser una dependencia.
* Ofrecen una funcionalidad pensada para ser reusada por otro proyecto.
* Usan el `setup.py` (`pip install`).
* Suelen alojarse en un index (PyPI u otros).
* Tiene dependencias **abstractas**.

## Aplicaciones

* Estan pensadas para uso final.
* No son instalables (un script que corre indefinidamente).
* Ofrecen un servicio
* No están pensadas para ser dependencia.
* Usan un `requirement.txt` para configurar un entorno virtual de ejecución.
* Tienen dependencias **concretas**.

