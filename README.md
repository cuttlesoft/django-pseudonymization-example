# Django Pseudonymization Example
## Data Masking via Properties

This example Django app demonstrates an approach to pseudonymizing personal data using properties on the model.

### Implementation

The general steps involved in this approach:
* Create a custom User class
* Alter the model fields used for storage of values to be masked
* Add getter/setter methods for interacting with the unmasked values
* Create a custom User manager and queryset for basic filtering
* Create custom User admin and admin form classes for management

<!-- For a step-by-step guide through the code, check out [the companion blog post](#example-1). -->

### Important Note

Our `mask`/`unmask` functions are intended for this example only, to enable demonstration of the application's handling of masking and unmasking. They do not sufficiently protect the data, as it is reasonably likely that someone accessing the data would be able to simply reverse the shifted characters, re-identifying users without any additional information present.
