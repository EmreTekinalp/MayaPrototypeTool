[![Build Status](https://travis-ci.org/EmreTekinalp/MayaPrototypeTool.svg?branch=master)](https://travis-ci.org/EmreTekinalp/MayaPrototypeTool)
[![Test Coverage](https://api.codeclimate.com/v1/badges/478fc671accdf4a37c88/test_coverage)](https://codeclimate.com/github/EmreTekinalp/MayaPrototypeTool/test_coverage)

# MPT - MayaPrototypeTool
Generate Python Code of manually prototyped node network setups in Maya.
The basic idea stems from the fact that a Maya user creates and tests or in other words “prototypes” a setup inside Maya to see if it works before the user starts to write down that setup in python code, which can be tedious and time consuming at the same time. So the basic idea is to run the tool once this prototype is done to give the user a python code version of their creation.

Fundamentally the Maya vanilla code generation should be the core functionality.
The goal for later versions is to include external code in form of functions, classes, modules in the code generation process.