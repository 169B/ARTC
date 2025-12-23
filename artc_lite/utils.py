"""
Utility functions for ARTC-LITE.
"""

import numpy as np
from typing import Union, List


def validate_data(data: Union[np.ndarray, List[float]]) -> np.ndarray:
    """
    Validate and convert input data to numpy array.
    
    Args:
        data: Input data as numpy array or list
        
    Returns:
        Validated numpy array
        
    Raises:
        ValueError: If data is invalid
    """
    if isinstance(data, list):
        data = np.array(data, dtype=np.float32)
    else:
        data = np.asarray(data, dtype=np.float32)
    
    if len(data) == 0:
        return data
    
    if not np.all(np.isfinite(data)):
        raise ValueError("Data contains NaN or infinite values")
    
    return data


def format_bytes(num_bytes: int) -> str:
    """
    Format bytes into human-readable string.
    
    Args:
        num_bytes: Number of bytes
        
    Returns:
        Formatted string (e.g., "1.5 KB")
    """
    for unit in ['B', 'KB', 'MB', 'GB']:
        if num_bytes < 1024.0:
            return f"{num_bytes:.1f} {unit}"
        num_bytes /= 1024.0
    return f"{num_bytes:.1f} TB"
