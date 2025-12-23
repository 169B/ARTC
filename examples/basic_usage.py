"""
ARTC-LITE Basic Usage Example

This example demonstrates the fundamental operations of ARTC-LITE:
- Creating a compressor
- Compressing data
- Viewing statistics
- Decompressing data
- Verifying accuracy
"""

from artc_lite import ARTCLITE
import numpy as np


def main():
    print("=" * 70)
    print("ARTC-LITE: Basic Usage Example")
    print("=" * 70)
    
    # Step 1: Generate some sample data
    print("\n📊 Step 1: Generate sample data")
    print("-" * 70)
    
    # Create simple linear temperature data (simulating a warming trend)
    data = np.linspace(20, 25, 100)  # Temperature from 20°C to 25°C
    print(f"Generated {len(data)} temperature readings")
    print(f"Range: {data[0]:.1f}°C to {data[-1]:.1f}°C")
    print(f"First 5 values: {data[:5]}")
    
    # Step 2: Create compressor
    print("\n🗜️  Step 2: Create ARTCLITE compressor")
    print("-" * 70)
    
    compressor = ARTCLITE(
        block_size=8,     # Process 8 values at a time
        tolerance=0.2     # Allow 0.2°C error
    )
    print(f"Created compressor with block_size={compressor.block_size}, tolerance={compressor.tolerance}")
    
    # Step 3: Compress the data
    print("\n📦 Step 3: Compress the data")
    print("-" * 70)
    
    compressed = compressor.compress(data)
    print(f"Compressed into {len(compressed)} blocks")
    
    # Step 4: View statistics
    print("\n📈 Step 4: View compression statistics")
    print("-" * 70)
    
    compressor.print_stats()
    
    # Step 5: Examine compressed data structure
    print("\n🔍 Step 5: Examine compressed data structure")
    print("-" * 70)
    
    print("First compressed block:")
    print(f"  Type: {compressed[0]['type']}")
    if compressed[0]['type'] == 'formula':
        print(f"  Formula: y = {compressed[0]['m']:.4f}x + {compressed[0]['b']:.4f}")
        print(f"  Size: 8 bytes (just two numbers!)")
    else:
        print(f"  Raw data: {len(compressed[0]['data'])} values")
        print(f"  Size: {len(compressed[0]['data']) * 4} bytes")
    
    # Step 6: Decompress
    print("\n🔄 Step 6: Decompress the data")
    print("-" * 70)
    
    decompressed = compressor.decompress(compressed)
    print(f"Decompressed {len(decompressed)} values")
    
    # Step 7: Verify accuracy
    print("\n✅ Step 7: Verify accuracy")
    print("-" * 70)
    
    max_error = np.max(np.abs(data[:len(decompressed)] - decompressed))
    mean_error = np.mean(np.abs(data[:len(decompressed)] - decompressed))
    
    print(f"Maximum error: {max_error:.6f}°C")
    print(f"Mean error: {mean_error:.6f}°C")
    print(f"Tolerance: {compressor.tolerance}°C")
    
    if max_error <= compressor.tolerance:
        print("\n🎉 SUCCESS! All values within tolerance")
    else:
        print("\n⚠️  WARNING: Some values exceed tolerance")
    
    # Summary
    print("\n" + "=" * 70)
    print("Summary")
    print("=" * 70)
    print(f"Original size:    {compressor.stats['original_size']:4d} bytes")
    print(f"Compressed size:  {compressor.stats['compressed_size']:4d} bytes")
    print(f"Compression ratio: {compressor.get_ratio():.1f}x")
    print(f"Space saved:      {compressor.stats['original_size'] - compressor.stats['compressed_size']:4d} bytes ({(1 - 1/compressor.get_ratio())*100:.0f}%)")
    print("=" * 70)


if __name__ == "__main__":
    main()
