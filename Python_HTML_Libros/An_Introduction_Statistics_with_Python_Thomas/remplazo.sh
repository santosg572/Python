#!/bin/bash

texbuscar=$1
texremp=$2
archivo=$3

sed -i "s/$texbuscar/$texremp/g" $archivo


