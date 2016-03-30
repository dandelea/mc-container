# mc-container
Aplicación para la tarea 04 de MC (Matemática Computacional) del Máster de Ingeniería Informática de la Universidad de Sevilla.

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
