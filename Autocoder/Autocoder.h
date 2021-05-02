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

extern "C"{

    void deleteVector(char* v){
        delete[] v;
    }

    Autocoder* createAutocoder(int chunkSize, int to){
        return new Autocoder(chunkSize, to);
    }

    void deleteAutocoder(Autocoder* a){
        delete a;
    }

    void learn(Autocoder* a, const char* data){
        a->learn(std::string(data));
    }

    char* encode(Autocoder* a, const char* dat){
        std::string data(dat);
        std::vector<bool> code = a->encode(data);
        char* res = new char[code.size()];
        for(size_t i = 0; i < code.size(); ++i){
            res[i] = '0' + code[i];
        }
        return res;
    }

    char* decode(Autocoder* a, const char* cod){
        std::vector<bool> code(strlen(cod));
        for(size_t i = 0; i < strlen(cod); ++i){
            code[i] = cod[i];
        }
        std::string decoded = a->decode(code);
        char* decode = new char[decoded.size()];
        for(size_t i = 0; i < decoded.size(); ++i){
            decode[i] = decoded[i];
        }
        return decode;
    }



    std::vector<bool> getRaw(const std::string& s);

    std::vector<std::vector<bool>> getInput(const std::string& data, size_t chunkSize);

    std::string makeString(std::vector<bool>& data);

    char* stupid_function(char* s){
        std::string str(s);
        char* c = new char[str.size()];
        for(size_t i = 0; i < str.size(); ++i){
            c[i] = str[i];
        }
        return c;
    }
}
