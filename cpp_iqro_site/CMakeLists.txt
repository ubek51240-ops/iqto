cmake_minimum_required(VERSION 3.10)
project(cpp_iqro_site CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(cpp_iqro_site main.cpp)

if(WIN32)
    target_link_libraries(cpp_iqro_site ws2_32)
endif()
