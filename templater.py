#!/usr/bin/python3
"""
FILE: templater.py
AUTHOR: Dylan (zinglax) Zingler
DATE: Sept 6 2018
PURPOSE: Manage & utilize JSON files & Jinja2 templates to create documents.

"""
import jinja2
import json
import os

# Local.
import config

class Templater():
    """Template manager"""

    def __init__(self):
        self.template_dirs = [x[0] for x in os.walk(config.TEMPLATE_DIR)]
        self.template_env = self.create_jinja2_env(template_dirs=self.template_dirs)

    def create_jinja2_env(self, **kwargs):
        """A jinja2 Environment with templates loaded.
        Args:
            **kwargs (TYPE): Description
        """
        if "template_dirs" in kwargs:
            template_loader = jinja2.FileSystemLoader(kwargs["template_dirs"])
        template_env = jinja2.Environment(loader=template_loader)
        return template_env

    def render(self, template, data):
        """Render templated data""" 
        rendered_data = self.template_env.get_template(template).render(data=data)
        return rendered_data

    def render_file(self, out_file, template, data):
        """Render a file with given data and template""" 
        rendered_data = self.render(template, data)
        with open(out_file, "w+") as f:
            f.write(rendered_data) 



