""" Configuration Specification (template) Module
    Creates the configSpec string for QCOBJ

    RV 20170906
    RV 20180904
"""
from __future__ import print_function
from collections import OrderedDict as Odict

# Local imports
from qcobj.qconfigobj import makeSpec, MANY, reindent

#------------------------------------------------------------------------------
level = 0
# This is the root section
secname = ''
#------------------------------------------------------------------------------
subsection = Odict((
     ('description', dict(comments=[
        '',
        'A descripion of this configuration file',
        '',],
        units='string',
        default='A meaningful descripion of this configuration file')),
    ('voltage', dict(comments='The voltage applied', units='V',
        min=0, max=100, default=13.8)),
    ('C', dict(comments='The capacitance of the capacitor', units='F',
        min=0, max=1000, default=0.1)),
    ('UG', dict(comments='Universal gravity constant',
        units='N * m**2 / kg**2', default=6.672e-11)),
    ('numberOfSteps', dict(comments='Maximum number of steps',
        units='int', min=0, max=5, default=1)),
    ('myrange', dict(comments='The allowed range', units='float',
        min=-5.5, max=14.4, default=12.0)),
    ('cake', dict(comments=['The cake that we will eat', 'this evening'],
        units="none Sacher Saint-Honore apple-pie".split(),
        default='Sacher')),
    ('approximate', dict(comments='Use approximation', units='boolean',
        default=False)),
    ('color_index', dict(comments='The color index', units='dimensionless',
        default=1.0)),
    ('configFiles', dict(comments='List of more configuration files blank'
        ' separated', units='string', default='')),
    ))
rootSpec = makeSpec(secname, subsection, level)
# Remove indentation
rootspec = "\n".join([line.lstrip() for line in rootSpec.splitlines()])

#------------------------------------------------------------------------------
level = 1
secname = 'Ingredients'
#------------------------------------------------------------------------------
subsection = Odict((
    ('sugar', dict(comments='Enable sugar', units='boolean',
        default=False)),
    ('fruits', dict(comments='A list of two fruits at your choice',
        units='string_list 2 2', default="apple, orange")),
    ('roomTemp', dict(comments='Room temperature', units='degC',
        min=18, max=26, default=20.0)),
    ('fraction', dict(comments='Some decimal value (floats are welcome,'
        ' as always)', units='float', min=0, max=1, default=0.25)),
    ))
subspec = makeSpec(secname, subsection, level)

#------------------------------------------------------------------------------
level = 2
secname = 'Regions'
#------------------------------------------------------------------------------
subsection = Odict((
    ('enabled', dict(comments='Enable all regions', units='boolean',
        default=False)),
    ))
subsubspec = makeSpec(secname, subsection, level)

level += 1
secname = MANY
subsection = Odict((
    ('enabled', dict(comments='Enable this region', units='boolean',
        default=False)),
    ('T', dict(comments='Constant Temperature', units='degC',
        default=18.0)),
    ('polygons', dict(comments=['Polygons defined by their vertices,'
        ' one per line,', 'separated by nl'], units='string', default="")),
    ))
many = makeSpec(secname, subsection, level)

morespec = """
#
# More Sections like this can be added with different names
# (e.g. region1, region2, ...) and the same syntax:
#
"""

configSpec = '\n'.join((
    rootspec,
    subspec,
    subsubspec,
    reindent(morespec, level * 4),
    many,
    ))

if __name__ == '__main__':
    configspecFile = "configspec.cfg"
    with open(configspecFile, "w") as out:
        out.write(configSpec)
    print("%s has been created" % configspecFile)
