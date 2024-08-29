cmake_minimum_required(VERSION 3.10)

# Project name
project(MyProject)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Include directory for header files
include_directories(include)

# Add the executable target
add_executable(MyProject C:/Users/MartinezR/SemanticAlgo/MyProject/src/main.cpp C:/Users/MartinezR/SemanticAlgo/MyProject/src/foo.cpp)

# Add the test executable target
add_executable(TestFoo C:/Users/MartinezR/SemanticAlgo/MyProject/tests/test_foo.cpp C:/Users/MartinezR/SemanticAlgo/MyProject/src/foo.cpp)
