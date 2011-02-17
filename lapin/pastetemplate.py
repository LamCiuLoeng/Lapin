# -*- coding: utf-8 -*-

from paste.script import templates

class LapinTemplate(templates.Template):

    egg_plugins = ['Framework']
    summary = 'Lapin Standard Quickstart Template'
    _template_dir = 'template'
