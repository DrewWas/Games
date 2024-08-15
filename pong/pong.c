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
    
    window = SDL_CreateWindow("Pong in C", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, WIDTH, HEIGHT, SDL_WINDOW_SHOWN); 


    /* Show window on monitor rather than main screen This needs to be edited if not using a monitor, but then again, all these programs are only meant to be played on a specific monitor size/dimension (mine) */

    SDL_Rect displayBounds;
    SDL_GetDisplayBounds(1, &displayBounds);
    SDL_SetWindowPosition(window, displayBounds.x + 200, displayBounds.y + 200);
    renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED); 


    // Main event loop
    while (!quit) {
        while (SDL_PollEvent(&event) != 0) {
            if (event.type == SDL_QUIT) {
                quit = 1;
                break;
            }
        }



        // Redraw everything
        SDL_SetRenderDrawColor(renderer, 0, 138, 255, 0);
        SDL_RenderClear(renderer);
        SDL_RenderPresent(renderer);
        SDL_Delay(60);

    } 

    return 0;

}



