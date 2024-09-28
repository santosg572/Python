#!/bin/bash

pdflatex ${1}.tex

okular ${1}.pdf &


