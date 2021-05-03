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
        std::string str(code.size(),'a');
        for(size_t i = 0; i < code.size(); ++i){
            str[i] = '0' + code[i];
        }
        char* res = new char(str.length());
        strcpy(res, str.c_str());
        return res;
    }

    char* decode(Autocoder* a, const char* cod){
        std::string code(cod);
        std::vector<bool> v(code.size());
        for(size_t i = 0; i < code.size(); ++i){
            v[i] = code[i] - '0';
        }
        std::string decoded = a->decode(v);
        char* decode = new char[decoded.size()];
        strcpy(decode, decoded.c_str());
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

    void print(char* c){
        std::cout << c << '\n';
    }
}
