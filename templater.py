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
        self.template_env = self.create_jinja2_env(template_dirs=[config.OUTPUT_DIR])
        

    def create_jinja2_env(self, **kwargs):
        """A jinja2 Environment with templates loaded.
        Args:
            **kwargs (TYPE): Description
        """
        if "template_dirs" in kwargs:
            template_loader = jinja2.FileSystemLoader(kwargs["template_dirs"])
        template_env = jinja2.Environment(loader=template_loader)
        return template_env


