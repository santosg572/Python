get_data_home
======================

Help on function get_data_home in module seaborn.utils:

get_data_home(data_home=None)
    Return a path to the cache directory for example datasets.

    This directory is used by :func:`load_dataset`.

    If the ``data_home`` argument is not provided, it will use a directory
    specified by the `SEABORN_DATA` environment variable (if it exists)
    or otherwise default to an OS-appropriate user cache location.

