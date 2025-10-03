#!/bin/bash

#ls -1 /vagrant/Pubmed_Resultados_ene1625/intelligence_20*.txt

dir=(
"/vagrant/Pubmed_Resultados_ene1625/intelligence_2005"
"/vagrant/Pubmed_Resultados_ene1625/intelligence_2006"
"/vagrant/Pubmed_Resultados_ene1625/intelligence_2007"
"/vagrant/Pubmed_Resultados_ene1625/intelligence_2008" 
"/vagrant/Pubmed_Resultados_ene1625/intelligence_2009" 
"/vagrant/Pubmed_Resultados_ene1625/intelligence_2010" 
"/vagrant/Pubmed_Resultados_ene1625/intelligence_2011" 
"/vagrant/Pubmed_Resultados_ene1625/intelligence_2012" 
"/vagrant/Pubmed_Resultados_ene1625/intelligence_2013" 
"/vagrant/Pubmed_Resultados_ene1625/intelligence_2014" 
"/vagrant/Pubmed_Resultados_ene1625/intelligence_2015" 
"/vagrant/Pubmed_Resultados_ene1625/intelligence_2016" 
"/vagrant/Pubmed_Resultados_ene1625/intelligence_2017" 
"/vagrant/Pubmed_Resultados_ene1625/intelligence_2018" 
"/vagrant/Pubmed_Resultados_ene1625/intelligence_2019" 
"/vagrant/Pubmed_Resultados_ene1625/intelligence_2020" 
"/vagrant/Pubmed_Resultados_ene1625/intelligence_2021" 
"/vagrant/Pubmed_Resultados_ene1625/intelligence_2022" 
"/vagrant/Pubmed_Resultados_ene1625/intelligence_2023" 
"/vagrant/Pubmed_Resultados_ene1625/intelligence_2024" 
"/vagrant/Pubmed_Resultados_ene1625/intelligence_2025" 
"/vagrant/Pubmed_Resultados_ene1625/intelligence_2026" 
"/vagrant/Pubmed_Resultados_ene1625/intelligence_2027" 
"/vagrant/Pubmed_Resultados_ene1625/intelligence_2028" 
"/vagrant/Pubmed_Resultados_ene1625/intelligence_2029")



for dd in "${dir[@]}"
do
    echo $dd
#  ./saca_titulos.sh $dd
  python traduce_tutulos_2.py $dd
done



