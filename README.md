# ARTC - Adaptive Regression Tensor Compression

A family of compression algorithms optimized for different use cases. 

## Variants

### ARTC:  General Adaptive Regression Tensor Compression
**For:** Any data, any use case

### ARTC-LITE:  Lightweight IoT Tensor Encoding
**For:** IoT sensors, embedded devices, battery-powered systems

```python
from artc import ARTCLITE

# Temperature sensor example
compressor = ARTCLITE(block_size=8, tolerance=0.1)
compressed = compressor.compress(sensor_data)
compressor.print_stats()
```

**Benefits:**
- 2-10× compression on smooth sensor data
- Minimal RAM usage (~50 bytes)
- Fast (< 1ms per block)
- Easy to port to C/Arduino

### ARTC-VRAM *(Coming Soon)*
**For:** GPU memory compression, fitting bigger AI models

### ARTC - FLEX *(Coming Soon)*
**For:** Formula-based Lightweight Efficient eXtended (memory) - ARTC for AI/MLs for GPUs.


---

## Installation

```bash
pip install artc
```

Or install from source:

```bash
git clone https://github.com/169B/artc.git
cd artc
pip install -e .
```

## How It Works

ARTC-LITE finds patterns in smooth data by fitting simple formulas. 

```
Input:  [20.0, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5]  (32 bytes)
Pattern: Goes up by 0.5 each time
Formula: y = 0.5x + 20.0
Stored:   m=0.5, b=20.0  (8 bytes)
Result:  4× smaller
```

## Comparison

| Method | Sensor Data | Random Data | Speed | RAM |
|--------|-------------|-------------|-------|-----|
| **ARTC-LITE** | **2-10×** | ~1× | ***~50 bytes** |
| GZIP | 1.1× | 1-2× | Medium | ~32 KB |


## License

GNU Generic 3.0
