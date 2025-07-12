"""
SimpleLombok - Example usage

This file demonstrates the various features of the SimpleLombok library.
"""
from simple_lombok import (
    # Basic decorators
    getter, setter, getter_and_setter,

    # Data class functionality
    data_class, equals_and_hash_code, to_string,

    # Constructor functionality
    all_args_constructor, no_args_constructor, required_args_constructor, builder,

    # Validation functionality
    validate_field, not_null, range_check, string_length, pattern, ValidationError,

    # Immutable functionality
    immutable, frozen_dataclass, with_method, ImmutableError
)

from simple_lombok import Logger

logger = Logger()
logger.error("Hello, world!")
logger.info("Hello, world!")
logger.warn("Hello, world!")
logger.success("Hello, world!")
logger.debug("Hello, world!")

