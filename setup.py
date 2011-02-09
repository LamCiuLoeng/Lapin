# -*- coding: utf-8 -*-
#===============================================================================
# 
#===============================================================================

from setuptools import setup, find_packages
setup(
        name = 'Lapin',
        version = '0.01a1',
        description = 'A flask-based web framework',
        keywords = 'Lapin Python Framework',
        author = 'CL.Lam',
        author_email = 'lamciuloeng@gmail.com',
        url = 'http://lapin.sys2do.com',
        license = "MIT",
        zip_safe = False,
        install_requires = ["flask>=0.6", "PasteScript>=1.7",
#                            "SQLAlchemy>=0.65" 
                            ],
        packages = find_packages(exclude = ['ez_setup', 'examples', 'tests']),
        include_package_data = True,
        entry_points = """
        [paste.paster_command]
        lapin_start = lapin.command:StartCommand
        
        [paste.global_paster_command]
        lapin_start = lapin.command:StartCommand
        
        [paste.paster_create_template]
        lapin_template = lapin.pastetemplate:LapinTemplate
        """)
