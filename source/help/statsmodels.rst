Help on package statsmodels:
============================

NAME
    statsmodels

PACKAGE CONTENTS

    * _version
    * api
    * base (package)
    * compat (package)
    * conftest
    * datasets (package)
    * discrete (package)
    * distributions (package)
    * duration (package)
    * emplike (package)
    * formula (package)
    * gam (package)
    * genmod (package)
    * graphics (package)
    * imputation (package)
    * interface (package)
    * iolib (package)
    * miscmodels (package)
    * multivariate (package)
    * nonparametric (package)
    * othermod (package)
    * regression (package)
    * robust (package)
    * sandbox (package)
    * src (package)
    * stats (package)
    * tests (package)
    * tools (package)
    * treatment (package)
    * tsa (package)

FUNCTIONS
    test(extra_args=None, exit=False)
        Run the test suite
        
        Parameters
        ----------
        extra_args : list[str]
            List of argument to pass to pytest when running the test suite. The
            default is ['--tb=short', '--disable-pytest-warnings'].
        exit : bool
            Flag indicating whether the test runner should exit when finished.
        
        Returns
        -------
        int
            The status code from the test run if exit is False.

DATA
    __all__ = ['__version__', '__version_info__', '__version_tuple__', 'te...
    __version_info__ = (0, 14, 5)
    __version_tuple__ = (0, 14, 5)

VERSION
    0.14.5

FILE
    /Users/santosg/miniconda3/lib/python3.9/site-packages/statsmodels/__init__.py


**Help on package statsmodels.stats in statsmodels:**

NAME
    statsmodels.stats

PACKAGE CONTENTS

    * _adnorm
    * _delta_method
    * _diagnostic_other
    * _inference_tools
    * _knockoff
    * _lilliefors
    * _lilliefors_critical_values
    * anova
    * api
    * base
    * contingency_tables
    * contrast
    * correlation_tools
    * descriptivestats
    * diagnostic
    * diagnostic_gen
    * dist_dependence_measures
    * effect_size
    * gof
    * inter_rater
    * knockoff_regeffects
    * libqsturng (package)
    * mediation
    * meta_analysis
    * moment_helpers
    * multicomp
    * multitest
    * multivariate
    * multivariate_tools
    * nonparametric
    * oaxaca
    * oneway
    * outliers_influence
    * power
    * proportion
    * rates
    * regularized_covariance
    * robust_compare
    * sandwich_covariance
    * stattools
    * tabledist
    * tests (package)
    * weightstats

DATA
    test = <statsmodels.tools._test_runner.PytestTester object>

FILE
    /Users/santosg/miniconda3/lib/python3.9/site-packages/statsmodels/stats/__init__.py


**Help on module statsmodels.stats.anova in statsmodels.stats:**

NAME
    statsmodels.stats.anova

CLASSES
    builtins.object
        AnovaRM
        AnovaResults
    
    class AnovaRM(builtins.object)
     |  AnovaRM(data, depvar, subject, within=None, between=None, aggregate_func=None)
     |  
     |  Repeated measures Anova using least squares regression
     |  
     |  The full model regression residual sum of squares is
     |  used to compare with the reduced model for calculating the
     |  within-subject effect sum of squares [1].
     |  
     |  Currently, only fully balanced within-subject designs are supported.
     |  Calculation of between-subject effects and corrections for violation of
     |  sphericity are not yet implemented.
     |  
     |  Parameters
     |  ----------
     |  data : DataFrame
     |  depvar : str
     |      The dependent variable in `data`
     |  subject : str
     |      Specify the subject id
     |  within : list[str]
     |      The within-subject factors
     |  between : list[str]
     |      The between-subject factors, this is not yet implemented
     |  aggregate_func : {None, 'mean', callable}
     |      If the data set contains more than a single observation per subject
     |      and cell of the specified model, this function will be used to
     |      aggregate the data before running the Anova. `None` (the default) will
     |      not perform any aggregation; 'mean' is s shortcut to `numpy.mean`.
     |      An exception will be raised if aggregation is required, but no
     |      aggregation function was specified.
     |  
     |  Returns
     |  -------
     |  results : AnovaResults instance
     |  
     |  Raises
     |  ------
     |  ValueError
     |      If the data need to be aggregated, but `aggregate_func` was not
     |      specified.
     |  
     |  Notes
     |  -----
     |  This implementation currently only supports fully balanced designs. If the
     |  data contain more than one observation per subject and cell of the design,
     |  these observations need to be aggregated into a single observation
     |  before the Anova is calculated, either manually or by passing an aggregation
     |  function via the `aggregate_func` keyword argument.
     |  Note that if the input data set was not balanced before performing the
     |  aggregation, the implied heteroscedasticity of the data is ignored.
     |  
     |  References
     |  ----------
     |  .. [*] Rutherford, Andrew. Anova and ANCOVA: a GLM approach. John Wiley & Sons, 2011.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, data, depvar, subject, within=None, between=None, aggregate_func=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  fit(self)
     |      estimate the model and compute the Anova table
     |      
     |      Returns
     |      -------
     |      AnovaResults instance
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class AnovaResults(builtins.object)
     |  AnovaResults(anova_table)
     |  
     |  Anova results class
     |  
     |  Attributes
     |  ----------
     |  anova_table : DataFrame
     |  
     |  Methods defined here:
     |  
     |  __init__(self, anova_table)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __str__(self)
     |      Return str(self).
     |  
     |  summary(self)
     |      create summary results
     |      
     |      Returns
     |      -------
     |      summary : summary2.Summary instance
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)

FUNCTIONS
    anova1_lm_single(model, endog, exog, nobs, design_info, table, n_rows, test, pr_test, robust)
        Anova table for one fitted linear model.
        
        Parameters
        ----------
        model : fitted linear model results instance
            A fitted linear model
        
        **kwargs**
        
        scale : float
            Estimate of variance, If None, will be estimated from the largest
        model. Default is None.
            test : str {"F", "Chisq", "Cp"} or None
            Test statistics to provide. Default is "F".
        
        Notes
        -----
        Use of this function is discouraged. Use anova_lm instead.
    
    anova2_lm_single(model, design_info, n_rows, test, pr_test, robust)
        Anova type II table for one fitted linear model.
        
        Parameters
        ----------
        model : fitted linear model results instance
            A fitted linear model
        
        **kwargs**
        
        scale : float
            Estimate of variance, If None, will be estimated from the largest
        model. Default is None.
            test : str {"F", "Chisq", "Cp"} or None
            Test statistics to provide. Default is "F".
        
        Notes
        -----
        Use of this function is discouraged. Use anova_lm instead.
        
        Type II
        Sum of Squares compares marginal contribution of terms. Thus, it is
        not particularly useful for models with significant interaction terms.
    
    anova3_lm_single(model, design_info, n_rows, test, pr_test, robust)
    
    anova_lm(*args, **kwargs)
        Anova table for one or more fitted linear models.
        
        Parameters
        ----------
        args : fitted linear model results instance
            One or more fitted linear models
        scale : float
            Estimate of variance, If None, will be estimated from the largest
            model. Default is None.
        test : str {"F", "Chisq", "Cp"} or None
            Test statistics to provide. Default is "F".
        typ : str or int {"I","II","III"} or {1,2,3}
            The type of Anova test to perform. See notes.
        robust : {None, "hc0", "hc1", "hc2", "hc3"}
            Use heteroscedasticity-corrected coefficient covariance matrix.
            If robust covariance is desired, it is recommended to use `hc3`.
        
        Returns
        -------
        anova : DataFrame
            When args is a single model, return is DataFrame with columns:
        
            sum_sq : float64
                Sum of squares for model terms.
            df : float64
                Degrees of freedom for model terms.
            F : float64
                F statistic value for significance of adding model terms.
            PR(>F) : float64
                P-value for significance of adding model terms.
        
            When args is multiple models, return is DataFrame with columns:
        
            df_resid : float64
                Degrees of freedom of residuals in models.
            ssr : float64
                Sum of squares of residuals in models.
            df_diff : float64
                Degrees of freedom difference from previous model in args
            ss_dff : float64
                Difference in ssr from previous model in args
            F : float64
                F statistic comparing to previous model in args
            PR(>F): float64
                P-value for significance comparing to previous model in args
        
        Notes
        -----
        Model statistics are given in the order of args. Models must have been fit
        using the formula api.
        
        See Also
        --------
        model_results.compare_f_test, model_results.compare_lm_test
        
        Examples
        --------
        >>> import statsmodels.api as sm
        >>> from statsmodels.formula.api import ols
        >>> moore = sm.datasets.get_rdataset("Moore", "carData", cache=True) # load
        >>> data = moore.data
        >>> data = data.rename(columns={"partner.status" :
        ...                             "partner_status"}) # make name pythonic
        >>> moore_lm = ols('conformity ~ C(fcategory, Sum)*C(partner_status, Sum)',
        ...                 data=data).fit()
        >>> table = sm.stats.anova_lm(moore_lm, typ=2) # Type 2 Anova DataFrame
        >>> print(table)
    
    anova_single(model, **kwargs)
        Anova table for one fitted linear model.
        
        Parameters
        ----------
        model : fitted linear model results instance
            A fitted linear model
        typ : int or str {1,2,3} or {"I","II","III"}
            Type of sum of squares to use.
        
        **kwargs**
        
        scale : float
            Estimate of variance, If None, will be estimated from the largest
        model. Default is None.
            test : str {"F", "Chisq", "Cp"} or None
            Test statistics to provide. Default is "F".
        
        Notes
        -----
        Use of this function is discouraged. Use anova_lm instead.

FILE
    /Users/santosg/miniconda3/lib/python3.9/site-packages/statsmodels/stats/anova.py


None
