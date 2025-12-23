"""
ARTC-LITE: Lightweight IoT Tensor Encoding
===========================================

Ultra-lightweight compression for IoT sensor data using adaptive regression.

Example:
    >>> from artc_lite import ARTCLITE
    >>> import numpy as np
    >>> 
    >>> data = np.linspace(20, 25, 100)
    >>> compressor = ARTCLITE(block_size=8, tolerance=0.2)
    >>> compressed = compressor.compress(data)
    >>> compressor.print_stats()
"""

from .core import ARTCLITE
from .version import __version__

__all__ = ['ARTCLITE', '__version__']
