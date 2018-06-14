# Django Pseudonymization Example

This example Django app demonstrates two approaches to pseudonymizing personal data with masking functions<!--  as outlined in [this blog post]() -->.

- [Example 1](https://github.com/cuttlesoft/django-pseudonymization-example/tree/properties) employs getter and setter methods to interface with the pseudonymized model fields.
- [Example 2](https://github.com/cuttlesoft/django-pseudonymization-example/tree/fields) creates a custom Field class to handle value masking/unmasking automatically.
