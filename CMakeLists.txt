cmake_minimum_required(VERSION 3.16)
project(autopilot)

set(CMAKE_CXX_STANDARD 17)

find_package(GTest REQUIRED)

include_directories(include)

#add_executable(hello_world
#        src/hello_world.cpp)

add_executable(test
        src/hello_world.cpp
        test/hello_world_test.cpp)
target_link_libraries(test gtest pthread)