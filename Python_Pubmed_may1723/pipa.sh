#!/bin/bash

palabra="machine learning"
file1="machine_learning"

python buscar.py "${palabra}" "${file1}" 

python resumen.py "${file1}"







