#include <SDL.h>
#include <SDL_ttf.h>
#include <stdio.h>
#include <time.h>


void drawBall(SDL_Renderer *renderer, int ball_x, int ball_y, int radius) {
    for (int x = -radius; x <= radius; x++) {
        for (int y = -radius; y <= radius; y++) {
            if ((x*x) + (y*y) < (radius * radius)) {
                SDL_RenderDrawPoint(renderer, ball_x + x, ball_y + y);
            }
        }
    }
}


void homeScreen(SDL_Renderer* renderer, TTF_Font* font_big, 
    TTF_Font* font_small, SDL_Color white, SDL_Color blue, SDL_Color red, int DIFFICULTY) {

    char difficultyText[50];
    snprintf(difficultyText, sizeof(difficultyText), "Difficulty: %d", DIFFICULTY);

    SDL_Surface* surface1 = TTF_RenderText_Solid(font_big, "Welcome to Pong in C !", blue);
    SDL_Surface* surface2 = TTF_RenderText_Solid(font_small, "Click Spacebar to Play", white);
    SDL_Surface* surface3 = TTF_RenderText_Solid(font_small, difficultyText, red); 

    SDL_Texture* surface1Texture = SDL_CreateTextureFromSurface(renderer, surface1);
    SDL_Texture* surface2Texture = SDL_CreateTextureFromSurface(renderer, surface2);
    SDL_Texture* surface3Texture = SDL_CreateTextureFromSurface(renderer, surface3);

    SDL_FreeSurface(surface1);
    SDL_FreeSurface(surface2);
    SDL_FreeSurface(surface3);
    SDL_Rect destRect1 = {350, 250, surface1->w, surface1->h};
    SDL_Rect destRect2 = {510, 400, surface2->w, surface2->h};
    SDL_Rect destRect3 = {620, 475, surface3->w, surface3->h};

    SDL_SetRenderDrawColor(renderer, 0, 0, 0, 0);
    SDL_RenderClear(renderer);

    SDL_RenderCopy(renderer, surface1Texture, NULL, &destRect1);
    SDL_RenderCopy(renderer, surface2Texture, NULL, &destRect2);
    SDL_RenderCopy(renderer, surface3Texture, NULL, &destRect3);
    SDL_RenderPresent(renderer);

    SDL_Delay(5);
}


void gameOver(SDL_Renderer* renderer, TTF_Font* font_big, 
    TTF_Font* font_small, SDL_Color white, SDL_Color blue, SDL_Color red) {


    SDL_Surface* surface1 = TTF_RenderText_Solid(font_big, "Game Over :(", red);
    SDL_Surface* surface2 = TTF_RenderText_Solid(font_small, "Click Spacebar to play again or q to exit", blue);
    SDL_Surface* surface3 = TTF_RenderText_Solid(font_small, "Select a number (1-3) to play again with a new difficulty", white); 

    SDL_Texture* surface1Texture = SDL_CreateTextureFromSurface(renderer, surface1);
    SDL_Texture* surface2Texture = SDL_CreateTextureFromSurface(renderer, surface2);
    SDL_Texture* surface3Texture = SDL_CreateTextureFromSurface(renderer, surface3);

    SDL_FreeSurface(surface1);
    SDL_FreeSurface(surface2);
    SDL_FreeSurface(surface3);
    SDL_Rect destRect1 = {500, 250, surface1->w, surface1->h};
    SDL_Rect destRect2 = {335, 400, surface2->w, surface2->h};
    SDL_Rect destRect3 = {210, 500, surface3->w, surface3->h};

    SDL_SetRenderDrawColor(renderer, 0, 0, 0, 0);
    SDL_RenderClear(renderer);

    SDL_RenderCopy(renderer, surface1Texture, NULL, &destRect1);
    SDL_RenderCopy(renderer, surface2Texture, NULL, &destRect2);
    SDL_RenderCopy(renderer, surface3Texture, NULL, &destRect3);
    SDL_RenderPresent(renderer);

    SDL_Delay(5);

}


int main(int argc, char* argv[]) {

    // Setup and Constants
    SDL_Window* window;
    SDL_Renderer* renderer;
    SDL_Event event;
    int gameOverScreen = 0;
    int DIFFICULTY = 1;
    int homeScreenStart = 1;
    int quit = 0;
    int WIDTH = 1500;
    int HEIGHT = 750;
    int player1_score = 0;
    int player2_score = 0;
    SDL_Color BLUE = {0, 138, 255};
    SDL_Color WHITE = {255, 255, 255};
    SDL_Color RED = {255, 0, 0};
    int result = SDL_Init(SDL_INIT_EVERYTHING);
    

    // Game Constants
    srand(time(NULL));
    int player1_y = 100 + rand() % 501;
    int player2_y = 100 + rand() % 501;  
    int ball_x = 750;
    int ball_y = 375;
    int ball_x_velo = 12;
    int ball_y_velo = 12; 

    // Player 1
    SDL_Rect player1;
    player1.x = 10;
    player1.y = player1_y;
    player1.w = 15;
    player1.h = 120;

    // Player 2 
    SDL_Rect player2;
    player2.x = 1475;
    player2.y = player2_y;
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
    TTF_Font* pixelFontLarge = TTF_OpenFont("Helpers/fontpixel.ttf", 70);
    TTF_Font* pixelFontMed = TTF_OpenFont("Helpers/fontpixel.ttf", 40);


    int keyState[SDL_NUM_SCANCODES] = {0};

    // Main event loop
    while (!quit) {
        const Uint8 *state;
        state = SDL_GetKeyboardState(NULL);

        // Homescreen loop
        while (homeScreenStart) {
             while (SDL_PollEvent(&event) != 0) {
                 if (event.type == SDL_QUIT) {
                     homeScreenStart = 0;
                     quit = 1;
                     break;
                 }
             }

            if (state[SDL_SCANCODE_SPACE]) {
                homeScreenStart = 0;
            }
            if (state[SDL_SCANCODE_Q]) {
                homeScreenStart = 0;
                quit = 1;
            }

            homeScreen(renderer, pixelFontLarge, pixelFontMed, WHITE, BLUE, RED, DIFFICULTY);
        }


        // Game loop
        while (SDL_PollEvent(&event) != 0) {
            if (event.type == SDL_QUIT) {
                quit = 1;
                break;
            }
        }

        if (state[SDL_SCANCODE_Q]) {
            quit = 1;
        }

        // Update player position based on key states
        if (state[SDL_SCANCODE_W] && player1.y > 10) {
            player1.y -= 18; 
        }

        if (state[SDL_SCANCODE_S] && player1.y < 620) {
            player1.y += 18;
        }

        if (state[SDL_SCANCODE_UP] && player2.y > 10) {
            player2.y -= 18; 
        }

        if (state[SDL_SCANCODE_DOWN] && player2.y < 620) {
            player2.y += 18; 
        }

        // Update score text
        char score1Text[10];
        sprintf(score1Text, "%d", player1_score);
        SDL_Surface* p1ScoreSurface= TTF_RenderText_Solid(pixelFontLarge, score1Text, WHITE);
        SDL_Texture* p1ScoreTexture = SDL_CreateTextureFromSurface(renderer, p1ScoreSurface);
        SDL_FreeSurface(p1ScoreSurface);
        SDL_Rect destRect1 = {1050, 50, p1ScoreSurface->w, p1ScoreSurface->h};

        char score2Text[10];
        sprintf(score2Text, "%d", player2_score);
        SDL_Surface* p2ScoreSurface = TTF_RenderText_Solid(pixelFontLarge, score2Text, WHITE);
        SDL_Texture* p2ScoreTexture = SDL_CreateTextureFromSurface(renderer, p2ScoreSurface);
        SDL_FreeSurface(p2ScoreSurface);
        SDL_Rect destRect2 = {350, 50, p2ScoreSurface->w, p2ScoreSurface->h};


        // Update ball position 
        ball_y -= ball_y_velo;
        ball_x += ball_x_velo;

        if (ball_x < 40 || ball_x > 1460) {
            if ((ball_x < 30) && (ball_y > player1.y - 10) && (ball_y < player1.y + 130)) {
                ball_x += 20;
                ball_x_velo *= -1;
                ball_x += 20;
            }
            else if ((ball_x > 1470) && (ball_y > player2.y - 10) && (ball_y < player2.y + 130)) {
                ball_x -= 20;
                ball_x_velo *= -1;
                ball_x -= 20;
            }
            else if (ball_x < -15|| ball_x > 1515){
                if (ball_x < 10) {
                    player2_score += 1;
                }
                else if (ball_x > 1490) {
                    player1_score += 1;
                }

                ball_x = 750;
                ball_y = 375;
                ball_x_velo *= -1;
            }
        }


        if (ball_y < 15 || ball_y > 735) {
            ball_y_velo *= -1;
        }


        // Check if game is over
        if (player1_score >= 11 || player2_score >= 11) {
            gameOverScreen = 1;
            SDL_Delay(10);
        }



        // Draw background 
        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 0);
        SDL_RenderClear(renderer);


        // Draw Scores 
        SDL_RenderClear(renderer);
        SDL_RenderCopy(renderer, p1ScoreTexture, NULL, &destRect1);
        SDL_RenderCopy(renderer, p2ScoreTexture, NULL, &destRect2);


        // Draw Ball
        SDL_SetRenderDrawColor(renderer, 255, 255, 255, 0);
        drawBall(renderer, ball_x, ball_y, 15); 


        // Draw Player1
        SDL_SetRenderDrawColor(renderer, 0, 138, 255, 0);
        SDL_RenderFillRect(renderer, &player1);

        // Draw Player2
        SDL_SetRenderDrawColor(renderer, 255, 0, 0, 0);
        SDL_RenderFillRect(renderer, &player2);

        // Update
        SDL_RenderPresent(renderer);
        SDL_Delay(5);

        while (gameOverScreen) {
             while (SDL_PollEvent(&event) != 0) {
                 if (event.type == SDL_QUIT) {
                     gameOverScreen = 0;
                     quit = 1;
                     break;
                 }
             }

            if (state[SDL_SCANCODE_SPACE]) {
                gameOverScreen = 0;
                homeScreenStart = 1;
                // Reset game info
                player1_score = 0;
                player2_score = 0;
                ball_x = 750;
                ball_y = 375;
                SDL_Delay(250); 
            }

            if (state[SDL_SCANCODE_1]) {
                gameOverScreen = 0;
                homeScreenStart = 1;
                // Reset game info
                player1_score = 0;
                player2_score = 0;
                ball_x = 750;
                ball_y = 375;
                DIFFICULTY = 1;
                ball_x_velo = 12;
                ball_x_velo = 12;
                SDL_Delay(100);
            }


            if (state[SDL_SCANCODE_2]) {
                gameOverScreen = 0;
                homeScreenStart = 1;
                // Reset game info
                player1_score = 0;
                player2_score = 0;
                ball_x = 750;
                ball_y = 375;
                DIFFICULTY = 2;
                ball_x_velo = 15;
                ball_x_velo = 15;
                SDL_Delay(100);
            }

            if (state[SDL_SCANCODE_3]) {
                gameOverScreen = 0;
                homeScreenStart = 1;
                // Reset game info
                player1_score = 0;
                player2_score = 0;
                ball_x = 750;
                ball_y = 375;
                DIFFICULTY = 3;
                ball_x_velo = 18;
                ball_y_velo = 18;
                SDL_Delay(100);
            }

            if (state[SDL_SCANCODE_Q]) {
                gameOverScreen = 0;
                quit = 1;
            }

            gameOver(renderer, pixelFontLarge, pixelFontMed, WHITE, BLUE, RED);
        }

    } 
    
    TTF_CloseFont(pixelFontLarge);
    TTF_CloseFont(pixelFontMed);
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    TTF_Quit();
    SDL_Quit();

    return 0;

}


