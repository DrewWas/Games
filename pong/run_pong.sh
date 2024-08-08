clang++ -std=c++17 -o pong_cpp pong.cpp $(pkg-config --cflags --libs sfml-graphics sfml-window sfml-system) && ./pong_cpp
