clang -std=c11 -o pong_c pong.c $(pkg-config --cflags --libs sdl2 sdl2_ttf) && ./pong_c
