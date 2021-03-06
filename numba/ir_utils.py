import numba.core.errors as _errors
from numba.core.utils import PYVERSION as _PYVERSION

_moved_mod = "numba.core.ir_utils"

if _PYVERSION >= (3, 7):
    __getattr__ = _errors.deprecate_moved_module_getattr(__name__, _moved_mod)
else:
    from numba.core.ir_utils import *  # noqa: F403, F401
    from numba.core.ir_utils import _max_label  # noqa: F401
    from numba.core.ir_utils import _add_alias  # noqa: F401

_errors.deprecate_moved_module(__name__, _moved_mod)
