from numba.core import types, config
from numba.core import errors
from numba.experimental.jitclass.base import register_class_type, ClassBuilder
import warnings


def jitclass(spec):
    """
    A decorator for creating a jitclass.

    **arguments**:

    - spec:
        Specifies the types of each field on this class.
        Must be a dictionary or a sequence.
        With a dictionary, use collections.OrderedDict for stable ordering.
        With a sequence, it must contain 2-tuples of (fieldname, fieldtype).

    **returns**:

    A callable that takes a class object, which will be compiled.
    """
    url = ("http://numba.pydata.org/numba-doc/latest/reference/"
           "deprecation.html#change-of-jitclass-location")

    msg = ("The 'numba.jitclass' decorator has moved to "
           "'numba.experimental.jitclass' to better reflect the experimental "
           "nature of the functionality. Please update your imports to "
           "accommodate this change and see {} for the time frame.".format(url))

    warnings.warn(msg, category=errors.NumbaDeprecationWarning,
                  stacklevel=2)

    def wrap(cls):
        if config.DISABLE_JIT:
            return cls
        else:
            return register_class_type(cls, spec, types.ClassType, ClassBuilder)

    return wrap
