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

    def render_template(self, out_file, template, data):
        """Render a file with given data and template""" 
        rendered_data = self.render(template, data)
 
        # Ensure parent output folder exists.
        out_folder = os.path.dirname(out_file)
        if not os.path.exists(out_folder):
            os.mkdir(out_folder)
            
        # Write rendered data to file. 
        with open(out_file, "w+") as f:
            f.write(rendered_data) 

    def render_json(self, out_file, template, json_file):
        """Renders a file based on a template and JSON data file"""
        
        # Ensure parent output folder exists.
        out_folder = os.path.dirname(out_file)

        if not os.path.exists(out_folder):
            raise ValueError("JSON File not found")
        with open(json_file) as f:
            json_data = json.load(f)
            self.render_template(out_file, template, json_data)

    def generate_info_json(self):
        """Create info JSON file that contains information about the Templater project"""
        # Date
        # Template Files
        # Info Files
        # Output Files
        # JSON Used
        pass







