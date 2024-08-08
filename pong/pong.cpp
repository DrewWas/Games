#include <SFML/Graphics.hpp>
#include <iostream>

int main() {


    // Create window 
    sf::RenderWindow window(sf::VideoMode(1500,750), "Pong C++");
    window.setFramerateLimit(60);


    // Create players  
    sf::RectangleShape player1;
    sf::Vector2f player1_pos(10, 120);
    player1.setPosition(player1_pos);
    player1.setSize(sf::Vector2f(20,120));
    player1.setFillColor(sf::Color::Red);

    sf::RectangleShape player2;
    sf::Vector2f player2_pos(1470, 120);
    player2.setPosition(player2_pos);
    player2.setSize(sf::Vector2f(20,120));
    player2.setFillColor(sf::Color::Blue);


    // Main game loop
    while (window.isOpen()) {
        
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed) {
                window.close();
            }


        }

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

        window.clear(sf::Color::Black);
        window.draw(player1);
        window.draw(player2);
        window.display();

    }

    

    return 0;


}




