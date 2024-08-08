#include <SFML/Graphics.hpp>
#include <iostream>
#include <random>
#include <ctime>

int main() {


    // Constants
    bool gameStarted = false;
    bool gameOver = false;

    // Create window 
    sf::RenderWindow window(sf::VideoMode(1500,750), "Pong C++");
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
    int ball_x_velo = 12;      // Change to be based on difficulty, which starts at 12 (this is hardcoded temporarily)
    int ball_y_velo = 12;
    sf::CircleShape ball(12);
    sf::Vector2f ball_pos(750, 375);
    ball.setPosition(ball_pos);
    


    // Create scores and print to screen
    int player1_score = 0;
    int player2_score = 0;

    sf::Font pixel_font;
    pixel_font.loadFromFile("Helpers/fontpixel.ttf");


    sf::Text player1_score_text;
    player1_score_text.setFont(pixel_font);
    player1_score_text.setString(std::to_string(player1_score));
    player1_score_text.setCharacterSize(70);
    player1_score_text.setPosition(350, 50);

    sf::Text player2_score_text;
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
        while (!gameStarted) { 

            sf::Text WelcomeText1;
            WelcomeText1.setFont(pixel_font);
            WelcomeText1.setString("Welcome to C++ Pong");
            WelcomeText1.setCharacterSize(70);
            WelcomeText1.setPosition(300, 250);

            WelcomeText1.setFillColor(sf::Color(0, 138, 255));


            if (sf::Keyboard::isKeyPressed(sf::Keyboard::Space)) {
                gameStarted = true;
            }

            window.clear(sf::Color::Black);
            window.draw(WelcomeText1);
            window.display();
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





