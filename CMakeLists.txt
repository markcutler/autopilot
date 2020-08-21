cmake_minimum_required(VERSION 3.16)
project(autopilot)

set(CMAKE_CXX_STANDARD 17)

find_package(GTest REQUIRED)

add_executable(test test/test.cpp)
target_link_libraries(test gtest pthread)