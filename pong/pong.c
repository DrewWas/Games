#include <SDL.h>
#include <stdio.h>


int main(int argc, char* argv[]) {

    // Setup and Constants
    SDL_Window* window;
    SDL_Renderer* renderer;
    SDL_Event event;
    int quit = 0;
    int WIDTH = 1500;
    int HEIGHT = 750;
    int result = SDL_Init(SDL_INIT_EVERYTHING);
    
    window = SDL_CreateWindow("Pong in C", 0, 0, WIDTH, HEIGHT, SDL_WINDOW_SHOWN); // SDL_WINDOWPOS_CENTERED

    SDL_DisplayMode displayMode;
    SDL_GetCurrentDisplayMode(1, &displayMode);

    int displayIndex = SDL_GetWindowDisplayIndex(window) + 2;
    printf("The window is on display index: %d\n", displayIndex);

    renderer = SDL_CreateRenderer(window, displayIndex, SDL_RENDERER_ACCELERATED); // Switch 2nd arg to -1

    while (!quit) {
        while (SDL_PollEvent(&event) != 0) {
            switch(event.type) {
                case SDL_QUIT:
                quit = 1;
                break;
            }
        }

        SDL_SetRenderDrawColor(renderer, 0,0,255,0);
        SDL_RenderClear(renderer);
        SDL_RenderPresent(renderer);
        SDL_Delay(60);

    } 

    return 0;

}


