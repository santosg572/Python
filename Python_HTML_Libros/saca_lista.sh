#!/bin/bash

pat=$1
file=$2

rm ${file}*

ls -1R ${pat} > "${file}.txt"

