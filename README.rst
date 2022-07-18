===============
Optimize Images
===============

``Optimize Images`` is a plugin for
`Pelican <http://docs.getpelican.com/>`_, a static site generator written
in Python.

``Optimize Images``  applies lossless compression on JPEG and PNG images,
with no effect on image quality. It uses jpegtran_ and OptiPNG_.

.. image:: https://img.shields.io/pypi/v/minchin.pelican.plugins.optimize-images.svg?style=flat
    :target: https://pypi.python.org/pypi/minchin.pelican.plugins.optimize-images/
    :alt: PyPI version number

.. image:: https://img.shields.io/badge/-Changelog-success
   :target: https://github.com/MinchinWeb/minchin.pelican.plugins.optimize_images/blob/master/CHANGELOG.rst
   :alt: Changelog

.. image:: https://img.shields.io/pypi/pyversions/minchin.pelican.plugins.optimize-images?style=flat
    :target: https://pypi.python.org/pypi/minchin.pelican.plugins.optimize-images/
    :alt: Supported Python version

.. image:: https://img.shields.io/pypi/l/minchin.pelican.plugins.optimize-images.svg?style=flat&color=green
    :target: https://github.com/MinchinWeb/minchin.pelican.plugins.optimize_images/blob/master/LICENSE.txt
    :alt: License

.. image:: https://img.shields.io/pypi/dm/minchin.pelican.plugins.optimize-images.svg?style=flat
    :target: https://pypi.python.org/pypi/minchin.pelican.plugins.optimize-images/
    :alt: Download Count


Installation
============

The easiest way to install ``Optimize Images`` is through the use of pip.
This will also install the required Python dependencies automatically.

.. code-block:: sh

  pip install minchin.pelican.plugins.optimize_images

It is assumed both jpegtran_ and OptiPNG_ are installed on system path.

If you are using Pelican 4.5, it should automatically be activated (through my
AutoLoader plugin). 

If you are using an earlier version of Pelican or autoloading isn't working,
then in your ``pelicanconf.py`` file, add ``Optimize Images`` to your list of
plugins:

.. code-block:: python

  PLUGINS = [
      # others...
      "minchin.pelican.plugins.optimize_images",
      # ...
  ]


Requirements
============

``Optimize Images`` depends on (and is really only useful with) Pelican.
This can be manually installed with pip:

.. code-block:: sh

   pip install pelican

It is assumed both jpegtran_ and OptiPNG_ are installed on system path. On
Windows, installers are available at each respective website. On Ubuntu
systems, the two can be installed via ``apt-get``:

.. code-block:: sh

  apt-get install optipng libjpeg-progs


Configuration and Usage
=======================

The plugin will activate and optimize images upon ``finalized`` signal of
pelican.

If add ``OPTIMIZE_IMAGES_DEV_MODE = True`` to your ``pelicanconf.py``, this
will disable the plugin, which is useful when developing your site locally.


Known Issues
============

Image manipulation like this can take some time to run. You may consider only
adding this plugin to your ``publishconf.py`` (rather than your base
``pelicanconf.py``) or add ``OPTIMIZE_IMAGES_DEV_MODE = True`` to your
``pelicanconf.py``, which will then only run this image optimization in
preparation for site publication.

An issue, as such, is that there is no formal test suite. Testing is
currently limited to my in-use observations. I also run a basic check upon
uploaded the package to PyPI that it can be downloaded and loaded into
Python.

The package is tested in Python 3.10; compatibility with other version of
Python is unknown, but there should be nothing particular keeping it from
working with other "modern" versions of Python.


Credits
=======

Original plugin from the `Pelican-Plugins repo
<https://github.com/getpelican/pelican-plugins>`_.


License
=======

The plugin code is assumed to be under the AGPLv3 license (this is the
license of the Pelican-Plugins repo).


.. _jpegtran: http://jpegclub.org/jpegtran/ 
.. _OptiPNG: http://optipng.sourceforge.net/
