.. Custom template for autosummary methods. Can be removed when
.. https://github.com/sphinx-doc/sphinx/issues/7912 is fixed.

{{ fullname | escape | underline}}

.. currentmodule:: {{ module }}

.. auto{{ objtype }}:: {{ objname }}
