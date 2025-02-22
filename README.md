# PLSE - Polish Lexical Scrabble Engine

PLSE (Polish Lexical Scrabble Engine) is a Python-based engine designed to help players of Scrabble in the Polish language find the best possible moves on a given board, based on a specific set of tiles. The engine employs an efficient algorithm for generating optimal moves in Scrabble, ensuring fast and accurate results.

This project is inspired by the "World’s Fastest Data Structures" paper by Andrew W. Appel and Guy J. Jacobson, and uses techniques outlined in the paper to accelerate the search for optimal Scrabble moves. The engine is optimized for Polish vocabulary and integrates seamlessly with any Scrabble board setup.

## Features

- **Optimal Move Search**: Given a Scrabble board and a set of tiles, the engine calculates the best possible moves using an efficient algorithm.
- **Polish Language Support**: The engine is tailored to work with the Polish dictionary sourced from the [SJP.pl dictionary](https://sjp.pl/sl/growy/), ensuring only valid Polish words are considered.
- **Fast Performance**: The algorithm is optimized for speed and handles large inputs quickly, making it ideal for both casual and competitive play.
- **Board Compatibility**: The engine can work with any Scrabble board setup, identifying valid moves based on current tile placements.

## Algorithm

PLSE is built on the principles of the algorithm described in the paper [The World’s Fastest Data Structures](https://www.cs.cmu.edu/afs/cs/academic/class/15451-s06/www/lectures/scrabble.pdf), which outlines a method for solving Scrabble using efficient data structures. By leveraging these advanced data structures, the engine is able to calculate the best possible Scrabble moves quickly and accurately.

## Dictionary Source

The dictionary used by PLSE is based on the data from the [SJP.pl dictionary](https://sjp.pl/sl/growy/), which provides a comprehensive list of valid Polish words that can be played in Scrabble. The dictionary is regularly updated and covers a wide range of Polish vocabulary, ensuring accuracy and consistency in the move suggestions.

## Contributing

We welcome contributions to improve the engine. If you'd like to help out, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit them (`git commit -am 'Add feature'`).
4. Push your changes to your fork (`git push origin feature/your-feature`).
5. Open a pull request to the main repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The algorithm used in this project is based on the work by Andrew W. Appel and Guy J. Jacobson, "The World’s Fastest Data Structures" ([Paper Link](https://www.cs.cmu.edu/afs/cs/academic/class/15451-s06/www/lectures/scrabble.pdf)).
- The PLSE engine uses the Polish lexicon sourced from the [SJP.pl dictionary](https://sjp.pl/sl/growy/), providing a comprehensive list of valid Polish Scrabble words.
