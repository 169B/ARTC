"""
Tests for ARTC-LITE streaming functionality.
"""

import pytest
import numpy as np
from artc_lite import ARTCLITE


class TestStreamingMode:
    """Test streaming mode operations."""
    
    def test_streaming_basic(self):
        """Test basic streaming operations."""
        compressor = ARTCLITE(block_size=8, tolerance=0.1)
        
        # Add readings one by one
        for i in range(8):
            compressor.add_reading(20.0 + i * 0.5)
        
        assert compressor.block_ready()
        block = compressor.get_block()
        
        assert block is not None
        assert block['type'] == 'formula'
    
    def test_streaming_multiple_blocks(self):
        """Test streaming with multiple blocks."""
        compressor = ARTCLITE(block_size=8, tolerance=0.1)
        blocks = []
        
        # Stream 24 values (3 blocks)
        for i in range(24):
            compressor.add_reading(float(i))
            if compressor.block_ready():
                blocks.append(compressor.get_block())
        
        assert len(blocks) == 3
        assert compressor.stats['blocks_compressed'] == 3
    
    def test_streaming_partial_block(self):
        """Test streaming with partial block at the end."""
        compressor = ARTCLITE(block_size=8)
        
        # Add 10 values (1 full block + 2 remaining)
        for i in range(10):
            compressor.add_reading(float(i))
            if compressor.block_ready():
                compressor.get_block()
        
        assert len(compressor._buffer) == 2
        assert not compressor.block_ready()
    
    def test_clear_buffer(self):
        """Test buffer clearing."""
        compressor = ARTCLITE(block_size=8)
        
        for i in range(5):
            compressor.add_reading(float(i))
        
        assert len(compressor._buffer) == 5
        compressor.clear_buffer()
        assert len(compressor._buffer) == 0
    
    def test_reset_stats(self):
        """Test statistics reset."""
        compressor = ARTCLITE(block_size=8, tolerance=0.1)
        
        # Process one block
        for i in range(8):
            compressor.add_reading(float(i))
        compressor.get_block()
        
        # Verify stats were updated
        assert compressor.stats['blocks_compressed'] > 0 or compressor.stats['blocks_raw'] > 0
        
        # Reset and verify
        compressor.reset_stats()
        assert compressor.stats['blocks_compressed'] == 0
        assert compressor.stats['blocks_raw'] == 0
        assert compressor.stats['original_size'] == 0
        assert compressor.stats['compressed_size'] == 0


class TestStreamingAccuracy:
    """Test streaming mode accuracy."""
    
    def test_streaming_vs_batch(self):
        """Test that streaming produces same results as batch."""
        np.random.seed(42)
        data = np.linspace(20, 30, 32) + np.random.normal(0, 0.01, 32)
        
        # Batch compression
        batch_compressor = ARTCLITE(block_size=8, tolerance=0.1)
        batch_compressed = batch_compressor.compress(data)
        
        # Streaming compression
        stream_compressor = ARTCLITE(block_size=8, tolerance=0.1)
        stream_compressed = []
        for value in data:
            stream_compressor.add_reading(value)
            if stream_compressor.block_ready():
                stream_compressed.append(stream_compressor.get_block())
        
        # Compare
        assert len(batch_compressed) == len(stream_compressed)
        
        # Decompress both and compare
        batch_decompressed = batch_compressor.decompress(batch_compressed)
        stream_decompressed = batch_compressor.decompress(stream_compressed)
        
        np.testing.assert_allclose(batch_decompressed, stream_decompressed, rtol=1e-5)
