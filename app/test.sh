#!/bin/bash
pylint -r y src
nosetests --with-coverage --cover-package=src
