#include <SDL.h>
#include <SDL2/SDL_ttf.h>
#include <stdio.h>


int main(int argc, char* argv[]) {

    // Setup and Constants
    SDL_Window* window;
    SDL_Renderer* renderer;
    SDL_Event event;
    int quit = 0;
    int WIDTH = 1500;
    int HEIGHT = 750;
    int player1_score = 0;
    int player2_score = 0;
    SDL_Color BLUE = {0, 138, 255};
    SDL_Color WHITE = {255, 255, 255};
    int result = SDL_Init(SDL_INIT_EVERYTHING);
    

    // Game Constants
    int player1_y = 300;  // Make random
    int player2_y = 300;  // Make random
    int ball_x = 750;
    int ball_y = 375;

    // Player 1
    SDL_Rect player1;
    player1.x = 10;
    player1.y = 300;
    player1.w = 15;
    player1.h = 120;

    // Player 2 
    SDL_Rect player2;
    player2.x = 1475;
    player2.y = 300;
    player2.w = 15;
    player2.h = 120;



    window = SDL_CreateWindow("Pong in C", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, WIDTH, HEIGHT, SDL_WINDOW_SHOWN); 


    /* Show window on monitor rather than main screen This needs to be edited if not using a monitor, but then again, all these programs are only meant to be played on a specific monitor size/dimension (mine) */

    SDL_Rect displayBounds;
    SDL_GetDisplayBounds(1, &displayBounds);
    SDL_SetWindowPosition(window, displayBounds.x + 200, displayBounds.y + 200);
    renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED); 


    // Font & Text Setup
    TTF_Init();
    TTF_Font* pixelFont = TTF_OpenFont("Helpers/fontpixel.ttf", 70);
    SDL_Surface* p1ScoreSurface = TTF_RenderText_Solid(pixelFont, " HELLO!!", WHITE);
    SDL_Texture* texture = SDL_CreateTextureFromSurface(renderer, p1ScoreSurface);


    int keyState[SDL_NUM_SCANCODES] = {0};
    // Main event loop
    while (!quit) {
        while (SDL_PollEvent(&event) != 0) {
            if (event.type == SDL_QUIT) {
                quit = 1;
                break;
            }
        }


        const Uint8 *state = SDL_GetKeyboardState(NULL);

        // Update player position based on key states

        if (state[SDL_SCANCODE_W] && player1.y > 10) {
            player1.y -= 15; 
        }

        if (state[SDL_SCANCODE_S] && player1.y < 620) {
            player1.y += 15;
        }

        if (state[SDL_SCANCODE_UP] && player2.y > 10) {
            player2.y -= 15; 
        }

        if (state[SDL_SCANCODE_DOWN] && player2.y < 620) {
            player2.y += 15; 
        }


        

        // Draw background 
        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 0);
        SDL_RenderClear(renderer);


        // Draw Scores 
        SDL_RenderCopy(renderer, texture, NULL, NULL);
        //SDL_RenderPresent(renderer);   (Why is this needed)??

        // Draw Ball


        // Draw Player1
        SDL_SetRenderDrawColor(renderer, 0, 138, 255, 0);
        SDL_RenderFillRect(renderer, &player1);

        // Draw Player2
        SDL_SetRenderDrawColor(renderer, 255, 0, 0, 0);
        SDL_RenderFillRect(renderer, &player2);

        // Update
        SDL_RenderPresent(renderer);
        SDL_Delay(5);

    } 
    
    SDL_DestroyTexture(texture);    
    SDL_FreeSurface(p1ScoreSurface);
    TTF_CloseFont(pixelFont);
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    TTF_Quit();
    SDL_Quit();

    return 0;

}



