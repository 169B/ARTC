# ARTC-LITE Documentation

Welcome to the ARTC-LITE documentation!

## What is ARTC-LITE?

ARTC-LITE (Adaptive Regression Tensor Compression - Lightweight IoT Tensor Encoding) is an ultra-lightweight compression algorithm designed specifically for IoT sensor data. It achieves 2-10× compression on smooth sensor readings while using minimal memory (~50 bytes RAM) and processing time (< 1ms per block).

## Quick Navigation

- **[Getting Started](tutorials/getting_started.md)** - Installation and first steps
- **[API Reference](api.md)** - Complete API documentation
- **[Algorithm Details](algorithm.md)** - How ARTC-LITE works
- **[Parameter Tuning](tutorials/parameter_tuning.md)** - Optimize for your use case
- **[Arduino Guide](tutorials/arduino_porting.md)** - Port to microcontrollers

## Quick Start

### Installation

```bash
pip install artc-lite
```

### Basic Example

```python
from artc_lite import ARTCLITE
import numpy as np

# Create compressor
compressor = ARTCLITE(block_size=8, tolerance=0.1)

# Compress data
data = np.linspace(20, 25, 100)
compressed = compressor.compress(data)

# View results
compressor.print_stats()
```

## Key Concepts

### Block Size
The number of sensor readings processed together. Smaller blocks use less RAM but may compress less effectively.

**Typical values:**
- Arduino Uno: 8-16
- ESP32: 16-32
- Raspberry Pi: 32-64

### Tolerance
Maximum acceptable error in reconstructed data. Higher tolerance allows better compression but less accuracy.

**Guidelines:**
- Temperature sensors: 0.1-0.5°C
- Pressure sensors: 0.01-0.1 hPa
- GPS coordinates: 0.0001-0.001°

### Compression Types

ARTC-LITE uses two compression strategies:

1. **Formula Compression**: Stores pattern as `y = mx + b` (8 bytes)
2. **Raw Fallback**: Stores original data when pattern doesn't fit

The algorithm automatically chooses the best option for each block.

## Support

- GitHub Issues: [https://github.com/169B/ARTC/issues](https://github.com/169B/ARTC/issues)

## License

MIT License - See [LICENSE](../LICENSE) for details.
