/*
 * ARTC-LITE Arduino Library Implementation
 * 
 * Author: 169B
 * License: MIT
 */

#include "artc_lite.h"

ARTCLITE::ARTCLITE(uint8_t blockSize, float tolerance) {
    this->blockSize = min(blockSize, ARTC_LITE_MAX_BLOCK_SIZE);
    this->tolerance = tolerance;
    this->bufferIndex = 0;
    resetStats();
}

// Rest of implementation would go here (truncated for brevity)
// See full implementation in Python version

void ARTCLITE::printStats() {
    Serial.println("==================================");
    Serial.println("ARTC-LITE Compression Stats");
    Serial.println("==================================");
    Serial.print("Total readings:     "); Serial.println(totalReadings);
    Serial.print("Original size:      "); Serial.print(originalSize); Serial.println(" bytes");
    Serial.print("Compressed size:    "); Serial.print(compressedSize); Serial.println(" bytes");
    Serial.print("Compression ratio:  "); Serial.print(getCompressionRatio()); Serial.println("x");
    Serial.println("==================================");
}

void ARTCLITE::resetStats() {
    totalReadings = 0;
    originalSize = 0;
    compressedSize = 0;
    blocksCompressed = 0;
    blocksRaw = 0;
}

float ARTCLITE::getCompressionRatio() {
    if (compressedSize == 0) return 1.0;
    return (float)originalSize / (float)compressedSize;
}
