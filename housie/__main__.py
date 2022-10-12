"""Convenience file to help start the game when the repo is cloned from git rather than installed via pip

This was required as we needed to run the script from the same level as the housie/ package in order for the imports
to work correctly.
"""
from .game import display_main_menu

display_main_menu()
