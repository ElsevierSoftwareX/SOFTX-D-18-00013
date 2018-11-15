.. _PySide: http://pyside.readthedocs.io/en/latest/building/

.. _PyQt4:  http://www.riverbankcomputing.co.uk/software/pyqt/download

.. _PyQt5:  https://pypi.org/project/PyQt5

.. _Pint:   http://pint.readthedocs.io/en/latest/

**********************************
QCOBJ Python Package Documentation
**********************************

Foreword
########
QCOBJ has been developed by two programmers working in the 
`Aerial Operations <http://www.inogs.it/en/content/aerial-operations>`_
group of the IRI Research Section at
`OGS - Istituto Nazionale di Oceanografia e di
Geofisica Sperimentale <http://www.inogs.it>`_.

Python is their favourite programming language since 2006.

The authors:

**Roberto Vidmar, Nicola Creati**

.. image:: images/vidmar.jpg
   :height: 134 px
   :width:  100 px 
.. image:: images/creati.jpg
   :height: 134 px
   :width:  100 px 

What is QCOBJ?
##############
Scientists often use configuration files (*cfg* files) to set the parameters
and              
initial conditions for their computer programs or simulations. When these       
parameters are not limited to numbers or strings but represent physical         
quantities their unit of measure must be taken into account.                    
Researchers are used to convert derived physical quantities by hand or          
with the help of some computer program but this operation slows down the
process        
and is inherently error prone.

**QCOBJ** tries                                 
to give an answer to this problem integrating unit of measure and hence   
dimensionality into parameters.
This approach ensures that programs using this package will always get        
numbers in the requested range and in the correct unit of measure               
independently of the units used in the configuration file.


QCOBJ in short
##############
  * create/edit configuration files with the power of
    `ConfigObj <http://configobj.readthedocs.io/en/latest/configobj.html>`_
  * mix physical quantities at your pleasure: specify pressure parameter
    like

    - pressure = 300.0 Pa *or*
    - pressure = 0.03 N / cm**2 *or*
    - pressure = 2.842 kgf / ft**2

    and let QCOBJ handle the conversion for you.
  * create validation files with physical quantities and valid range for
    all parameters.
  * use the validation file to define the preferred physical quantities
  * use :class:`qcobj.CfgGui` to develop your own Qt based GUI to show/edit
    configuration files.

Dependencies
############
It relies on
`ConfigObj <http://configobj.readthedocs.io/en/latest/configobj.html>`_,
Pint_ and PySide_ (or PyQt4_ / PyQt5_ , see :class:`qcobj.qtCompat`)
for the gui.

Credits
#######
This package was possible thanks to Hernan E. Grecco
<hernan.grecco@gmail.com> who released and
mantains Pint_ and helped in the integration.

.. note::
   The package depends on either PySide_ or PyQt (PyQt4_ / PyQt5_),
   and has
   ben tested with Python 3.4.3, 3.6.5, PySyde 1.2.4, PyQt4 4.8.1,
   PyQt5 5.10.1.

More
####
.. toctree::
  :maxdepth: 2

  CfgGui widget: <snapshots>

  QCOBJ Package Reference: <qcobj>

  A complex QCOBJ example file <fast19>

.. warning::
   This code has been tested *only* on Linux (Ubuntu 14.04.5 LTS and
   Kubuntu 17.10) but
   should work
   also on Mac and Windows (Xp and greater).

.. warning::
   This is work in progress!


Indices and Tables
##################
* :ref:`genindex`
* :ref:`modindex`
