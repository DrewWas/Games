clang -std=c11 -o pong_c pong.c $(pkg-config --cflags --libs sdl2) && ./pong_c
