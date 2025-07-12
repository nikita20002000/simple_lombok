"""
SimpleLombok - A Python library inspired by Java's Lombok.

This library provides decorators and utilities to reduce boilerplate code in Python classes.
It includes functionality for automatically generating getters, setters, constructors,
equality methods, string representations, and more.
"""

# Import decorators for getters and setters
from simple_lombok.decorators import getter, setter, getter_and_setter

# Import data class functionality
from simple_lombok.data_class import data_class, equals_and_hash_code, to_string

# Import constructor functionality
from simple_lombok.constructor import (
    all_args_constructor,
    no_args_constructor,
    required_args_constructor,
    builder
)

# Import validation functionality
from simple_lombok.validation import (
    validate_field,
    not_null,
    range_check,
    string_length,
    pattern,
    ValidationError
)

# Import immutable functionality
from simple_lombok.immutable import (
    immutable,
    frozen_dataclass,
    with_method,
    ImmutableError
)

# Import class Logger
from simple_lombok.logger import Logger

__all__ = [
    # Decorators
    'getter',
    'setter',
    'getter_and_setter',

    # Data class
    'data_class',
    'equals_and_hash_code',
    'to_string',

    # Constructor
    'all_args_constructor',
    'no_args_constructor',
    'required_args_constructor',
    'builder',

    # Validation
    'validate_field',
    'not_null',
    'range_check',
    'string_length',
    'pattern',
    'ValidationError',

    # Immutable
    'immutable',
    'frozen_dataclass',
    'with_method',
    'ImmutableError',

    # Logger
    'Logger'
]
