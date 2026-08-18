#!/bin/bash

rm Rplots.pdf
Rscript $1.R
open Rplots.pdf
