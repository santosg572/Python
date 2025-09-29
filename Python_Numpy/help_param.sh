#!/bin/bash

#dd=('abs' 'amax' 'append' 'apply_along_axis' 'apply_over_axes' 'arange' 'around' 'array' 
#'concatenate' 'cos' 
#'cumsum' 'delete' 'exp' 'eye' 'fmax' 'histogram' 'histogram2d' 'inf' 'insert' 'linspace' 
#'log10' 'matrix' 'max' 'mean' 'median' 
#'ones' 'percentile' 'pi' 'reshape' 'resize' 'round' 'shape' 'sin' 'size' 'sort' 'sqrt' 'sum' 
#'transpose' 'zeros')

dd=('beta' 'binomial' 'bit_generator' 'bytes' 'chisquare' 'choice' 'default_rng' 'dirichlet' 'exponential' 'f' 'gamma' 'geometric' 'get_state' 'gumbel' 'hypergeometric' 'laplace' 'logistic' 'lognormal' 'logseries' 'mtrand' 'multinomial' 'multivariate_normal' 'negative_binomial' 'noncentral_chisquare' 'noncentral_f' 'normal' 'pareto' 'permutation' 'poisson' 'power' 'rand' 'randint' 'randn' 'random' 'random_integers' 'random_sample' 'ranf' 'rayleigh' 'sample' 'seed' 'set_state' 'shuffle' 'standard_cauchy' 'standard_exponential' 'standard_gamma' 'standard_normal' 'standard_t' 'test' 'triangular' 'uniform' 'vonmises' 'wald' 'weibull' 'zipf' )

for ss in "${dd[@]}"
do
  echo $ss
  python help_param.py $ss > "help_"${ss}".txt"
done

