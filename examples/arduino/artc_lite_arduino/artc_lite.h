/*
 * ARTC-LITE Arduino Library
 * 
 * Lightweight compression for IoT sensor data
 * Perfect for Arduino, ESP32, and other microcontrollers
 * 
 * Author: 169B
 * License: MIT
 */

#ifndef ARTC_LITE_H
#define ARTC_LITE_H

#include <Arduino.h>

#define ARTC_LITE_MAX_BLOCK_SIZE 32
#define ARTC_LITE_FORMULA_TYPE 0
#define ARTC_LITE_RAW_TYPE 1

struct CompressedBlock {
    uint8_t type;           // ARTC_LITE_FORMULA_TYPE or ARTC_LITE_RAW_TYPE
    float m;                // Slope (for formula type)
    float b;                // Intercept (for formula type)
    float data[ARTC_LITE_MAX_BLOCK_SIZE];  // Raw data (for raw type)
    uint8_t data_length;    // Number of values in data array
};

class ARTCLITE {
public:
    ARTCLITE(uint8_t blockSize = 8, float tolerance = 0.1);
    
    // Batch compression
    bool compress(float* data, uint16_t length, CompressedBlock* output, uint16_t* numBlocks);
    bool decompress(CompressedBlock* blocks, uint16_t numBlocks, float* output, uint16_t* length);
    
    // Streaming mode
    void addReading(float value);
    bool blockReady();
    bool getBlock(CompressedBlock* output);
    void clearBuffer();
    
    // Statistics
    uint32_t getOriginalSize();
    uint32_t getCompressedSize();
    float getCompressionRatio();
    void printStats();
    void resetStats();
    
private:
    uint8_t blockSize;
    float tolerance;
    
    // Streaming buffer
    float buffer[ARTC_LITE_MAX_BLOCK_SIZE];
    uint8_t bufferIndex;
    
    // Statistics
    uint32_t totalReadings;
    uint32_t originalSize;
    uint32_t compressedSize;
    uint16_t blocksCompressed;
    uint16_t blocksRaw;
    
    // Internal methods
    bool compressBlock(float* block, uint8_t length, CompressedBlock* output);
    float calculateMean(float* data, uint8_t length);
};

#endif // ARTC_LITE_H
