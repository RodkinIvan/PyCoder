#pragma once
#include "Perceptron.h"



class Autocoder {
private:

    Perceptron<Sigmoid> p;
    size_t chunkSize = 0;
    size_t outSize = 0;

public:
    Autocoder(int chinkSize, int to);

    void learn(const std::string& data);

    std::vector<bool> encode(const std::string& data);

    std::string decode(const std::vector<bool>& code);
};

