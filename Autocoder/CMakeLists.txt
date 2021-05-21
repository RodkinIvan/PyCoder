cmake_minimum_required(VERSION 3.19)
project(Autocoder)

set(CMAKE_CXX_STANDARD 20)
set(LIBRARY_OUTPUT_PATH ${CMAKE_CURRENT_SOURCE_DIR}/lib)
add_library(Autocoder SHARED Perceptron.h Autocoder.h Autocoder.cpp)