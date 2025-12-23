# Sample IoT Sensor Data

This directory contains sample datasets for testing and demonstrating ARTC-LITE compression.

## Files

### temperature_sensor.csv
**Description**: 24-hour temperature readings from a room sensor  
**Expected Compression**: 3-5×

### conductivity_sensor.csv
**Description**: Water conductivity measurements  
**Expected Compression**: 4-6×

### gps_coordinates.csv
**Description**: GPS tracking of slow-moving object  
**Expected Compression**: 3-4× per channel

## Usage

```python
import pandas as pd
from artc_lite import ARTCLITE

# Load temperature data
df = pd.read_csv('data/temperature_sensor.csv')
temps = df['temperature'].values

# Compress
compressor = ARTCLITE(block_size=8, tolerance=0.1)
compressed = compressor.compress(temps)
compressor.print_stats()
```

## License

These sample datasets are provided under CC0 (Public Domain) for testing purposes.
