#!/usr/bin/python3
"""
FILE: tests.py
AUTHOR: Dylan (zinglax) Zingler
DATE: Sept 6 2018
PURPOSE: Unit tests for templater.py program.

"""
import unittest
import os
import jinja2

# Local.
import templater
import config

class TemplaterTests(unittest.TestCase):
    """Contains test cases for templater.py program"""

    def test_templater_initialization(self):
        """Test the creation of the templater class."""
        t = templater.Templater()
        self.assertIsNotNone(t)
       
    def test_templater_template_env_exists(self):
        """Test the creation of the templater template_env."""
        t = templater.Templater()
        self.assertIsNotNone(t.template_env)
        self.assertIsInstance(t.template_env, jinja2.environment.Environment)

    def test_templater_template_folder_exists(self):
        """Test templater input folder exists."""
        self.assertTrue(os.path.isdir(config.TEMPLATE_DIR))

    def test_templater_input_folder_exists(self):
        """Test templater input folder exists."""
        self.assertTrue(os.path.isdir(config.INPUT_DIR))

    def test_templater_output_folder_exists(self):
        """Test templater output folder exists."""
        self.assertTrue(os.path.isdir(config.OUTPUT_DIR))

    def test_templater_render_template(self):
        """Test templater info page"""
        # Remove existing file. 
        out_file = os.path.join(config.OUTPUT_DIR, "test", "test_document.html")
        if os.path.exists(out_file):
            os.remove(out_file)

        # Create templated file.
        t = templater.Templater()
        data = {}
        t.render_template(out_file, "test_document.html.jinja2", data)
        
        # Ensure output file exists.
        self.assertTrue(os.path.exists(out_file))

    def test_templater_render_json(self):
        """Test templater info page"""
        # Remove existing file. 
        out_file = os.path.join(config.OUTPUT_DIR, "test", "test_document.html")
        if os.path.exists(out_file):
            os.remove(out_file)
       
        # Create templated file.
        t = templater.Templater()
        json_file = os.path.join(config.INPUT_DIR, "test", "test_json.json")
        t.render_json(out_file, "test_json.html.jinja2", json_file)

        # Ensure output file exists.
        self.assertTrue(os.path.exists(out_file))

if __name__ == '__main__':
    unittest.main()


