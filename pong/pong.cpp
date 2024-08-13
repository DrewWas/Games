#include <SFML/Graphics.hpp>
#include <iostream>
#include <random>
#include <ctime>
#include <unistd.h>


// Constants (put into __init__ method??)
bool gameStarted = false;
bool gameOver = false;
int DIFFICULTY = 1;
int player1_score = 0; 
int player2_score = 0; 

sf::RenderWindow window(sf::VideoMode(1500,750), "Pong C++");
sf::Font pixel_font;
sf::Text player1_score_text;
sf::Text player2_score_text;

sf::Event event;

// Create homescreen
void homescreen() { 

    while (!gameStarted) {
        window.clear(sf::Color::Black);

        sf::Text WelcomeText1;
        WelcomeText1.setFont(pixel_font);
        WelcomeText1.setString("Welcome to C++ Pong");
        WelcomeText1.setCharacterSize(70);
        WelcomeText1.setPosition(350, 250);
        WelcomeText1.setFillColor(sf::Color(0, 138, 255));

        sf::Text WelcomeText2;
        WelcomeText2.setFont(pixel_font);
        WelcomeText2.setString("Click Spacebar To Play");
        WelcomeText2.setCharacterSize(40);
        WelcomeText2.setPosition(500, 400);

        sf::Text WelcomeText3;
        WelcomeText3.setFont(pixel_font);
        WelcomeText3.setString("Difficulty: " + std::to_string(DIFFICULTY));
        WelcomeText3.setCharacterSize(40);
        WelcomeText3.setPosition(620, 475);
        WelcomeText3.setFillColor(sf::Color::Red);

            while (window.pollEvent(event)) {
                if (event.type == sf::Event::Closed) {
                    window.close();
                    return;
                }
            }

            if (sf::Keyboard::isKeyPressed(sf::Keyboard::Q)) {
                window.close();
                return;
            }

            if (sf::Keyboard::isKeyPressed(sf::Keyboard::Space)) {
                gameStarted = true;
            }

            window.draw(WelcomeText1);
            window.draw(WelcomeText2);
            window.draw(WelcomeText3);
            window.display();
        }
}


// Create gameOverScreen
void gameOverScreen() {
    while (gameOver) {

        window.clear(sf::Color::Black);
        pixel_font.loadFromFile("Helpers/fontpixel.ttf");

        sf::Text GameOverText1;
        GameOverText1.setFont(pixel_font);
        GameOverText1.setString("Game Over :(");
        GameOverText1.setCharacterSize(70);
        GameOverText1.setPosition(500, 250);
        GameOverText1.setFillColor(sf::Color::Red);

        sf::Text GameOverText2;
        GameOverText2.setFont(pixel_font);
        GameOverText2.setString("Click Spacebar to play again or q to exit");
        GameOverText2.setCharacterSize(40);
        GameOverText2.setPosition(335, 400);
        GameOverText2.setFillColor(sf::Color(0, 138, 255));

        sf::Text GameOverText3;
        GameOverText3.setFont(pixel_font);
        GameOverText3.setString("Select a number (1-3) to play again with a new difficulty");
        GameOverText3.setCharacterSize(40);
        GameOverText3.setPosition(210, 500);
        GameOverText3.setFillColor(sf::Color::White);

        window.draw(GameOverText1);
        window.draw(GameOverText2);
        window.draw(GameOverText3);
        window.display();

        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed) {
                window.close();
                return;
            }

            if (sf::Keyboard::isKeyPressed(sf::Keyboard::Q)) {
                window.close();
                return;
            }

            if (sf::Keyboard::isKeyPressed(sf::Keyboard::Space)) {
                gameOver = false; 
                int sleep = 200000; // This sleep is so that when space is pressed the homescreen is not accidentally skipped 
                usleep(sleep);
                homescreen();  
            }

            if (sf::Keyboard::isKeyPressed(sf::Keyboard::Num1)) {
                DIFFICULTY = 1;
                gameOver = false;
                homescreen();
            }

            if (sf::Keyboard::isKeyPressed(sf::Keyboard::Num2)) {
                DIFFICULTY = 2;
                gameOver = false;
                homescreen();
            }

            if (sf::Keyboard::isKeyPressed(sf::Keyboard::Num3)) {
                DIFFICULTY = 3; 
                gameOver = false;
                homescreen();
            }
        
        }
    }
}



void resetGame() {
    player1_score = 0;
    player1_score_text.setString(std::to_string(player1_score));

    player2_score = 0;
    player2_score_text.setString(std::to_string(player2_score));
    //ball_x_velo = (adjust with difficulty)
    //ball_y_velo = (adjust with difficulty)
}



int main() {

    // Create window 
    window.setFramerateLimit(60);


    // Randomness for initial paddle positions
    std::default_random_engine generator(static_cast<unsigned>(std::time(nullptr)));
    std::uniform_int_distribution<int> distribution(100,600);

    int player1_initial = distribution(generator);
    int player2_initial = distribution(generator);


    // Create players  
    sf::RectangleShape player1;
    sf::Vector2f player1_pos(10, player1_initial);
    player1.setPosition(player1_pos);
    player1.setSize(sf::Vector2f(20,120));
    player1.setFillColor(sf::Color::Red);

    sf::RectangleShape player2;
    sf::Vector2f player2_pos(1470, player2_initial);
    player2.setPosition(player2_pos);
    player2.setSize(sf::Vector2f(20,120));
    player2.setFillColor(sf::Color(0, 138, 255)); // (0, 138, 255) is the RGB for a cleaner shade of blue

    // Create ball
    int ball_x_velo = 13;      // Change to be based on difficulty, which starts at 12 (this is hardcoded temporarily)
    int ball_y_velo = 13;
    sf::CircleShape ball(12);
    sf::Vector2f ball_pos(750, 375);
    ball.setPosition(ball_pos);
    
    pixel_font.loadFromFile("Helpers/fontpixel.ttf");

    player1_score_text.setFont(pixel_font);
    player1_score_text.setString(std::to_string(player1_score));
    player1_score_text.setCharacterSize(70);
    player1_score_text.setPosition(350, 50);

    player2_score_text.setFont(pixel_font);
    player2_score_text.setString(std::to_string(player2_score));
    player2_score_text.setCharacterSize(70);
    player2_score_text.setPosition(1050, 50);
    
    


    // Main game loop
    while (window.isOpen()) {
        
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed) {
                window.close();
            }

        }

        // Start game screen
        if (!gameStarted) {

            homescreen();

        }


        // Ball movement and logic
        ball_pos.x += ball_x_velo;
        ball_pos.y += ball_y_velo;



        // Player 1 movements
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::S) && player1_pos.y < 620) { 
            player1_pos.y += 12;
            player1.setPosition(player1_pos);
        }

        if (sf::Keyboard::isKeyPressed(sf::Keyboard::W) && player1_pos.y > 10) { 
            player1_pos.y -= 12;
            player1.setPosition(player1_pos);
        }

        // Player 2 movement
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Down) && player2_pos.y < 620) { 
            player2_pos.y += 12;
            player2.setPosition(player2_pos);
        }

        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Up) && player2_pos.y > 10) { 
            player2_pos.y -= 12;
            player2.setPosition(player2_pos);
        }


        // Ball paddle/wall collision logic
        if (ball_pos.x < 30) {

            if (player1_pos.y - 10 < ball_pos.y && ball_pos.y < player1_pos.y + 120 + 10) { 
                ball_pos.x += 10;
                ball_x_velo *= -1;
            }

            else if (ball_pos.x < -50) {
                ball_pos.x = 375;
                ball_x_velo *= -1;
                player2_score += 1;
                player2_score_text.setString(std::to_string(player2_score));
            }
        }
    
        else if (ball_pos.x > 1460) {

            if (player2_pos.y - 10 < ball_pos.y && ball_pos.y < player2_pos.y + 120 + 10) { 
                ball_pos.x -= 10;
                ball_x_velo *= -1;
            }

            else if (ball_pos.x > 1550) {
                ball_pos.x = 375;
                ball_x_velo *= -1;
                player1_score += 1;
                player1_score_text.setString(std::to_string(player1_score));
            }
        }

        if (ball_pos.y > 745 || ball_pos.y < 5) {
            ball_y_velo *= -1;
        }

        ball.setPosition(ball_pos);

        // Check player score
        if (player1_score >= 3 || player2_score >= 3) { // REVERT BACK TO 11!!
            gameOver = true;
            gameOverScreen();
            resetGame();
            gameStarted = false;
            continue;
        }


        window.clear(sf::Color::Black);
        window.draw(player1);
        window.draw(player2);
        window.draw(ball);
        window.draw(player1_score_text);
        window.draw(player2_score_text);
        window.display();

    }

    

    return 0;



}






