# Changelog

All notable changes to ARTC-LITE will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-12-23

### Added
- Complete package restructure to `artc-lite`
- Modern Python packaging with `pyproject.toml`
- Comprehensive test suite (37 tests across compression, streaming, visualization)
- Enhanced example scripts:
  - `basic_usage.py` - Simple introductory example
  - `sensor_demo.py` - Temperature sensor simulation
  - `streaming_demo.py` - Real-time streaming mode
- Arduino/C library stubs for embedded systems
- Test data files (linear, noisy, sensor CSV files)
- Utility functions module (`artc_lite/utils.py`)
- Version management system (`artc_lite/version.py`)

### Changed
- Renamed package from `artc` to `artc_lite`
- Updated all imports and references throughout codebase
- Modernized `setup.py` configuration
- Improved API documentation in docstrings
- Enhanced compression statistics display

### Fixed
- Package structure for better maintainability
- Import paths for Python 3.7+ compatibility
- Test coverage and reliability

### Development Status
- Upgraded from Alpha (3) to Beta (4)
- Production-ready for IoT sensor compression applications

## [0.1.0] - 2024-XX-XX

### Added
- Initial ARTC-LITE implementation
- Basic compression and decompression
- Streaming mode for real-time data
- Simple examples

[1.0.0]: https://github.com/169B/ARTC/releases/tag/v1.0.0
[0.1.0]: https://github.com/169B/ARTC/releases/tag/v0.1.0
