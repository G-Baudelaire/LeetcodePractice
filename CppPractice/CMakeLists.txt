cmake_minimum_required(VERSION 3.30)
project(LeetcodePractice)

set(CMAKE_CXX_STANDARD 26)

add_executable(
        CppPractice main.cpp
        Solution9.cpp
        Solution9.h
        Solution14.h
        Solution20.h
        Solution21.h
        Solution26.h
        Solution27.h
        Solution28.h
        Solution56.h
        Solution121.h
        Solution125.h
        Solution169.h
        Solution383.h
        Solution205.h
)

include_directories(.)