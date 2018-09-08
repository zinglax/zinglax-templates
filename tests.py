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


    def test_templater_info_page(self):
        """Test templater info page"""
        t = templater.Templater()





if __name__ == '__main__':
    unittest.main()


