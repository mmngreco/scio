# Branch naming

Buenas prácticas a la hora de poner nombres a ramas.

* https://nvie.com/posts/a-successful-git-branching-model/
   * https://gist.github.com/digitaljhelms/4287848
* https://docs.microsoft.com/en-us/azure/devops/repos/git/git-branching-guidance?view=azure-devops#name-your-feature-branches-by-convention

# Como escribir buenos mensajes en los commits

* https://chris.beams.io/posts/git-commit/
* https://github.com/erlang/otp/wiki/writing-good-commit-messages

# Como usar gitlab

Aunque parezca paradójico esto creo que hace falta:

https://about.gitlab.com/2018/03/05/gitlab-for-agile-software-development/

# Fomentar el uso de tox?

En los últimos días he incluido tox en mi workflow de desarrollo y he de decir
que me ha resultado de gran ayuda. Es increiblemente util y fácil de usar.

Aqui la docu:

* https://tox.readthedocs.io/en/latest/
* https://mviera.io/blog/automatizando-con-tox/

# Code review

Cómo hacer (y recibir) code reviews: https://phauer.com/2018/code-review-guidelines/

# Variables "secretas", seguridad, passwords

Una guía de buenas prácticas securizando variables:

https://www.freecodecamp.org/news/how-to-securely-store-api-keys-4ff3ea19ebda/

# Changelog

Todos los proyectos deberían incluir un changelog de los cambios realizados y
en proceso, aqui hay una guía muy buena que podría convertirse en un estándar perfectamente.


https://keepachangelog.com/es-ES/1.0.0/

# Pep8

Todos los proyectos en python deberían seguir el pep8 para un desarrollo homogéneo.

Herramientas que permiten seguir el complimiento:

* black
* flake8
* pylint


# Estructura `prj/src/prj`


* pros of src structure: https://hynek.me/articles/testing-packaging/#src
* pypa discussion and summary: https://github.com/pypa/packaging.python.org/issues/320#issuecomment-495990983
* now python recommends src structure: https://packaging.python.org/en/latest/tutorials/packaging-projects/#a-simple-project
