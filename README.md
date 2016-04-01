# mc-container
Aplicación para la tarea 04 de MC (Matemática Computacional) del Máster de Ingeniería Informática de la Universidad de Sevilla.

## Ejecución
* <code>python3 main.py</code>

## Instalación
* Actualizar las bases de datos de repositorios
 * <code>sudo apt-get update</code>
* Instalar Python 3.4:
 * <code>sudo apt-get install python3.4-dev</code>
* Instalar pip:
 * <code>wget https://bootstrap.pypa.io/get-pip.py</code>
 * <code>sudo python3 get-pip.py</code>
* Instalar numpy:
 * <code>pip install numpy</code>
* Instalar Matplotlib:
 * <code>sudo apt-get install tcl-dev tk-dev python-tk python3-tk</code>
 * <code>sudo apt-get install python-matplotlib</code>
 * <code>sudo apt-get build-dep python-matplotlib</code>
 * <code>cd ~</code>
 * <code>git clone https://github.com/matplotlib/matplotlib.git</code>
 * <code>cd matplotlib</code>
 * <code>python setup.py install</code>
* Instalar Numberjack y dependencias para Python3
 * <code>cd ~</code>
 * <code>wget ftp://xmlsoft.org/libxml2/libxml2-2.7.2.tar.gz</code>
 * <code>sudo tar xzf libxml2-2.7.2.tar.gz</code>
 * <code>cd libxml2-2.7.2</code>
 * <code>./configure</code>
 * <code>make</code>
 * <code>sudo make install</code>
 * <code>cd ~</code>
 * <code>sudo apt-get install swig</code>
 * <code>git clone https://github.com/eomahony/Numberjack</code>
 * <code>cd Numberjack</code>
 * <code>git fetch</code>
 * <code>git checkout -b Python3 origin/Python3</code>
 * <code>sudo python3 setup.py build</code>
 * <code>sudo python3 setup.py install</code>

## Referencias
* Hurley B. Numberjack. Combinatorial Optimization in Python. Pycon Ireland 2014. [online-PDF]. Disponible en http://numberjack.ucc.ie/sites/default/files/njpyconie14.pdf (Fecha de consulta: 1 de Abril de 2016).
* Hurley, B, O’Sullivan B. Problem Transformations and Algorithm Selection for CSPs. (Cork, Ireland) 2014. Proceedings of the Twenty-Third International Joint Conference on Artificial Intelligence. pp. 3221-3222.
* Le Berre and Lynce. A simple CSP to SAT Translator. Proceedings of the 2nd International CSP Solver Competition, 2008.
* Tamura N. System Description of a SAT-based CSP Solver Sugar  Proceedings of the 3rd International CSP Solver Competition, pp 71-75, 2009. 
* Tanjo T. Azucar: A SAT-based CSP Solver using Compact Order Encoding. 15th International Conference on Theory and Applications of Satisfiability Testing — SAT, pp 456–462, 2012.
* Bessiere C. Constraint Propagation. Technical Report LIRMM 06020. 2006 [online-PDF]. Disponible en ç http://www.lirmm.fr/~bessiere/stock/TR06020.pdf (Fecha de consulta: 1 de Abril de 2016).
* Problemas de satisfacción de restricciones (CSP). [online-PDF]. Disponible en http://users.dsic.upv.es/~msalido/papers/capitulo.pdf (Fecha de consulta: 1 de Abril de 2016).
* Numberjack. A platform for combinatorial optimization. 2013. [online-PDF]. Disponible en http://cp2013.a4cp.org/sites/default/files/uploads/cpsolvers2013.4C_0.pdf (Fecha de consulta: 1 de Abril de 2016).
* Hidalgo J, Turrado JI. Algoritmos genéticos: Aplicación al problema de la mochila. Universidad Carlos III de Madrid. [online-PDF] Disponible en http://www.it.uc3m.es/~jvillena/irc/practicas/10-11/01mem.pdf (Fecha de consulta: 1 de Abril de 2016).
* Emmanuel Hébrard, O’Mahony Eoin, O’Sullivan Barry. Constraing programming and combinatorial optimisation in Numberjack. 2011 [online-PDF] Disponible en https://hal-univ-tlse3.archives-ouvertes.fr/hal-00561698/document (Fecha de consulta: 1 de Abril de 2016).
