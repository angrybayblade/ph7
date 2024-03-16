# v0.1.0-rc5 (16-03-2024)

* Adds support for including CSS and JS files in separate blocks

# v0.1.0-rc4 (15-03-2024)

* Adds template engine for Flask
* Adds support for pseudo selector arguments via `__init_subclass__` method
* Adds support for returning iterables on the functional views

# v0.1.0-rc3 (12-03-2024)

* Adds support for named arguments on view based function
* Adds support for pseudo selectors
* Adds mock context and dry run support on the Django engine

# v0.1.0-rc2 (11-03-2024)

* Adds support for dry-runs on Django engine for functional resource collection
* Renames the `handlers` attribute to `on-*`
* Adds safe guard for missing  Django installation

# v0.1.0-rc1 (09-03-2024)

* Extends support for `document` API
* Adds support for transpiling
  *  `await` expressions
  *  String interpolations
  *  Dictionary declarations
  *  `try/except` blocks
  *  `raise` statement
* Better documentation for `Django` integrations