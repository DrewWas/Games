#include <SFML/Graphics.hpp>

int main() {

    // Create window 
    sf::RenderWindow window(sf::VideoMode(1500, 750), "Pong C++");

    // Main game loop
    while (window.isOpen()) {
        
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed) {
                window.close();
            }
        }


            // Testing drawing
            sf::RectangleShape rectangle(sf::Vector2f(120,50));
            rectangle.setSize(sf::Vector2f(100,100));
            window.draw(rectangle);

    }

    
    // window.clear(sf::Color::Black);

    // Testing drawing
    sf::RectangleShape rectangle(sf::Vector2f(120,50));
    rectangle.setSize(sf::Vector2f(100,100));
    window.draw(rectangle);

    window.display();

    return 0;


}




