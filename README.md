# ARTC - Adaptive Regression Tensor Compression

A family of compression algorithms optimized for different use cases. 

## Variants

### ARTC-LITE:  Lightweight IoT Tensor Encoding
**For:** IoT sensors, embedded devices, battery-powered systems

```python
from artc import ARTCLITE

# Temperature sensor example
compressor = ARTCLITE(block_size=8, tolerance=0.1)
compressed = compressor.compress(sensor_data)
compressor.print_stats()
```

**Perfect for:**
- ✅ Temperature, pressure, humidity sensors
- ✅ Arduino, ESP32, Raspberry Pi
- ✅ LoRa, Bluetooth, Zigbee wireless
- ✅ Solar/battery powered devices
- ✅ Slow networks (< 1 Mbps)

**Benefits:**
- 2-10× compression on smooth sensor data
- Minimal RAM usage (~50 bytes)
- Fast (< 1ms per block)
- Easy to port to C/Arduino

### ARTC-VRAM *(Coming Soon)*
**For:** GPU memory compression, fitting bigger AI models

### ARTC-IO *(Coming Soon)*
**For:** Network transfers, disk storage

---

## Installation

```bash
pip install artc
```

Or install from source:

```bash
git clone https://github.com/yourusername/artc.git
cd artc
pip install -e .
```

## Quick Start

```python
from artc import ARTCLITE
import numpy as np

# Sensor data
temps = np.array([20.1, 20.2, 20.3, 20.4, 20.5, 20.6, 20.7, 20.8])

# Compress
compressor = ARTCLITE()
compressed = compressor.compress(temps)

# Results
compressor.print_stats()
# Output: 
#   Original:   32 bytes
#   Compressed:  8 bytes
#   Ratio: 4.0x smaller

# Decompress
decompressed = compressor.decompress(compressed)
```

## Streaming Mode (Real-Time Sensors)

```python
compressor = ARTCLITE(block_size=8)

# Add readings as they come
for reading in sensor_stream():
    compressor.add_reading(reading)
    
    if compressor.block_ready():
        compressed = compressor.get_block()
        send_via_lora(compressed)  # Transmit
```

## Examples

See `examples/` directory:
- `lite_temperature.py` - Basic temperature sensor
- `lite_iot_demo.py` - Real-time streaming mode
- `lite_arduino.py` - Arduino/C port guide

Run examples:

```bash
python examples/lite_temperature.py
python examples/lite_iot_demo.py
python examples/lite_arduino.py
```

## How It Works

ARTC-LITE finds patterns in smooth data by fitting simple formulas. 

```
Input:  [20.0, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5]  (32 bytes)
Pattern: Goes up by 0.5 each time
Formula: y = 0.5x + 20.0
Stored:   m=0.5, b=20.0  (8 bytes)
Result:  4× smaller! 
```

## Comparison

| Method | Sensor Data | Random Data | Speed | RAM |
|--------|-------------|-------------|-------|-----|
| **ARTC-LITE** | **2-10×** | ~1× | **Very Fast** | **~50 bytes** |
| GZIP | 1.1× | 1-2× | Medium | ~32 KB |
| No compression | 1× | 1× | - | - |

## Testing

```bash
pip install pytest
pytest tests/
```

## License

MIT

## Contributing

Contributions welcome! This is an open research project.
