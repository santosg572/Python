#!/bin/bash

nom="twins"
diez=10

for i in {5..30}
do
  s="00"
  if [ $i -ge $diez ]
  then
    s="0"
  fi
  dd="TXT/"$nom"_2"$s$i
  ./saca_titulos.sh $dd
  echo $dd
done

