# Contributing to ARTC-LITE

First off, thank you for considering contributing to ARTC-LITE! It's people like you that make ARTC-LITE such a great tool for IoT compression.

## Code of Conduct

This project and everyone participating in it is governed by common sense and mutual respect. Be kind, be professional.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* **Use a clear and descriptive title**
* **Describe the exact steps to reproduce the problem**
* **Provide specific examples to demonstrate the steps**
* **Describe the behavior you observed and what behavior you expected**
* **Include code samples and test data if relevant**
* **Specify your Python version and operating system**

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

* **Use a clear and descriptive title**
* **Provide a detailed description of the suggested enhancement**
* **Explain why this enhancement would be useful**
* **Provide examples of how it would be used**

### Pull Requests

* Fill in the required template
* Follow the Python code style (PEP 8)
* Include tests for new functionality
* Update documentation as needed
* Ensure all tests pass before submitting

## Development Setup

### Prerequisites

* Python 3.7 or higher
* pip

### Setting Up Your Development Environment

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR-USERNAME/ARTC.git
   cd ARTC
   ```

3. Install in development mode:
   ```bash
   pip install -e ".[dev]"
   ```

4. Create a branch for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=artc_lite --cov-report=html
```

### Code Style

We follow PEP 8 style guide for Python code:

```bash
# Check style
flake8 artc_lite tests

# Auto-format code
black artc_lite tests
```

## Project Structure

```
artc_lite/          # Main package
├── __init__.py     # Package exports
├── core.py         # ARTCLITE class
├── utils.py        # Utility functions
└── version.py      # Version info

tests/              # Test suite
├── test_compression.py
├── test_streaming.py
└── test_visualization.py

examples/           # Example scripts
├── basic_usage.py
├── sensor_demo.py
└── streaming_demo.py
```

## Testing Guidelines

* Write tests for all new features
* Ensure tests are isolated and can run in any order
* Use descriptive test names: `test_compress_linear_data_with_small_tolerance`
* Include edge cases and error conditions
* Aim for >90% code coverage

## Documentation Guidelines

* Update docstrings for any changed functions/classes
* Follow NumPy docstring format
* Include code examples in docstrings
* Update README.md if adding major features
* Add entries to CHANGELOG.md

## Commit Message Guidelines

* Use present tense ("Add feature" not "Added feature")
* Use imperative mood ("Move cursor to..." not "Moves cursor to...")
* Start with a capital letter
* Keep first line under 72 characters
* Reference issues and pull requests after the first line

Example:
```
Add streaming mode support for multiple sensors

- Implement multi-channel streaming
- Add tests for concurrent streams
- Update documentation

Fixes #123
```

## Release Process

1. Update version in `artc_lite/version.py`
2. Update CHANGELOG.md
3. Create pull request for review
4. After merge, tag release: `git tag v1.0.0`
5. Push tag: `git push origin v1.0.0`

## Questions?

Feel free to open an issue with the "question" label.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
