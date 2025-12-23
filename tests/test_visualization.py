"""
Tests for ARTC-LITE visualization and statistics.
"""

import pytest
import numpy as np
from artc_lite import ARTCLITE
from io import StringIO
import sys


class TestStatistics:
    """Test compression statistics."""
    
    def test_get_ratio_perfect_compression(self):
        """Test compression ratio for perfect linear data."""
        compressor = ARTCLITE(block_size=8, tolerance=0.1)
        data = np.linspace(20, 28, 8).astype(np.float32)
        
        compressor.compress(data)
        
        ratio = compressor.get_ratio()
        assert ratio == 4.0  # 32 bytes -> 8 bytes
    
    def test_get_ratio_no_compression(self):
        """Test compression ratio when data doesn't compress."""
        compressor = ARTCLITE(block_size=8, tolerance=0.001)
        
        np.random.seed(42)
        data = np.random.randn(8).astype(np.float32)
        
        compressor.compress(data)
        
        ratio = compressor.get_ratio()
        assert ratio == 1.0  # No compression
    
    def test_stats_tracking(self):
        """Test that stats are tracked correctly."""
        compressor = ARTCLITE(block_size=8, tolerance=0.1)
        
        # 2 blocks of linear data
        data = np.linspace(0, 16, 16).astype(np.float32)
        compressor.compress(data)
        
        assert compressor.stats['total_readings'] == 16
        assert compressor.stats['original_size'] == 64  # 16 * 4 bytes
        assert compressor.stats['blocks_compressed'] == 2
        assert compressor.stats['blocks_raw'] == 0
    
    def test_mixed_compression_stats(self):
        """Test stats with mixed compressed and raw blocks."""
        compressor = ARTCLITE(block_size=8, tolerance=0.001)
        
        # Linear data + random data
        linear = np.linspace(0, 8, 8).astype(np.float32)
        np.random.seed(42)
        random = np.random.randn(8).astype(np.float32) * 10
        
        data = np.concatenate([linear, random])
        compressor.compress(data)
        
        # Linear should compress, random should not
        assert compressor.stats['blocks_compressed'] >= 1
        assert compressor.stats['blocks_raw'] >= 1
        
        total_blocks = compressor.stats['blocks_compressed'] + compressor.stats['blocks_raw']
        assert total_blocks == 2


class TestPrintStats:
    """Test statistics printing."""
    
    def test_print_stats_output(self):
        """Test that print_stats produces expected output."""
        compressor = ARTCLITE(block_size=8, tolerance=0.1)
        data = np.linspace(20, 28, 8).astype(np.float32)
        compressor.compress(data)
        
        # Capture output
        old_stdout = sys.stdout
        sys.stdout = captured_output = StringIO()
        
        compressor.print_stats()
        
        sys.stdout = old_stdout
        output = captured_output.getvalue()
        
        # Check key elements are present
        assert "ARTC-LITE" in output
        assert "Total readings" in output
        assert "Original size" in output
        assert "Compressed size" in output
        assert "Compression ratio" in output
        assert "4.0x" in output  # Perfect compression ratio
    
    def test_print_stats_success_rate(self):
        """Test that success rate is shown in stats."""
        compressor = ARTCLITE(block_size=8, tolerance=0.1)
        
        # Multiple blocks to get success rate
        data = np.linspace(0, 24, 24).astype(np.float32)
        compressor.compress(data)
        
        old_stdout = sys.stdout
        sys.stdout = captured_output = StringIO()
        
        compressor.print_stats()
        
        sys.stdout = old_stdout
        output = captured_output.getvalue()
        
        assert "Success rate" in output
        assert "100%" in output  # All blocks should compress
    
    def test_print_stats_empty(self):
        """Test print_stats with no data."""
        compressor = ARTCLITE(block_size=8)
        
        # Should not crash
        old_stdout = sys.stdout
        sys.stdout = captured_output = StringIO()
        
        compressor.print_stats()
        
        sys.stdout = old_stdout
        output = captured_output.getvalue()
        
        assert "ARTC-LITE" in output
        assert "0" in output  # Should show zeros


class TestVisualizationData:
    """Test data that could be visualized."""
    
    def test_compression_decision_tracking(self):
        """Test tracking which blocks compress vs raw."""
        compressor = ARTCLITE(block_size=8, tolerance=0.05)
        
        # Mix of compressible and incompressible data
        compressible = np.linspace(0, 8, 8).astype(np.float32)
        np.random.seed(42)
        incompressible = np.random.randn(8).astype(np.float32) * 10
        
        data = np.concatenate([compressible, incompressible])
        compressed = compressor.compress(data)
        
        # Check each block type
        assert compressed[0]['type'] == 'formula'
        assert compressed[1]['type'] == 'raw'
