# Django Pseudonymization Example
## Data Masking via Custom Fields

This example Django app demonstrates an approach to pseudonymizing personal data using custom fields on the model.

### Implementation

The general steps involved in this approach:
* Create a custom User class
* Create a custom Field class
    * `__init__` and `deconstruct`
    * `get_internal_type`
    * `get_prep_value` and `from_db_value`
* Alter the model fields used for storage of values to be masked

<!-- For a step-by-step guide through the code, check out [the companion blog post](#example-2). -->

### Important Note

Our `mask`/`unmask` functions are intended for this example only, to enable demonstration of the application's handling of masking and unmasking. They do not sufficiently protect the data, as it is reasonably likely that someone accessing the data would be able to simply reverse the shifted characters, re-identifying users without any additional information present.
