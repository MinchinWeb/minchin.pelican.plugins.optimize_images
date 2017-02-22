===============
Optimize Images
===============

``Optimize Images`` is a plugin for `Pelican <http://docs.getpelican.com/>`_,
a static site generator written in Python.

``Optimize Images``  applies lossless compression on JPEG and PNG images, with
no effect on image quality. It uses jpegtran_ and OptiPNG_.


Installation
============

The easiest way to install ``Optimize Images`` is through the use of pip. This
will also install the required Python dependencies automatically (currently none beyond Pelican itself).

.. code-block:: sh

  pip install minchin.pelican.plugins.optimize_images

It is assumed both jpegtran_ and OptiPNG_ are installed on system path.

Then, in your ``pelicanconf.py`` file, add ``Optimize Images`` to your list of
plugins:

.. code-block:: python

  PLUGINS = [
              # ...
              'minchin.pelican.plugins.optimize_images',
              # ...
            ]


Requirements
============

``Optimize Images`` depends on (and is really only useful with) Pelican. This can
be manually installed with pip:

.. code-block:: sh

   pip install pelican

It is assumed both jpegtran_ and OptiPNG_ are installed on system path. On Windows, installers are available at each respective website. On Ubuntu systems, the two can be installed via ``apt-get``.

.. code-block:: sh

  apt-get install optipng libjpeg-progs


Configuration and Usage
=======================

The plugin will activate and optimize images upon ``finalized`` signal of
pelican.

The plugin has no user settings.


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
