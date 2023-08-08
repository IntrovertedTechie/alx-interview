#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

// Check if movieId is provided
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movieId>');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const film = JSON.parse(body);
    const characters = film.characters;

    characters.forEach((characterUrl) => {
      request(characterUrl, (characterError, characterResponse, characterBody) => {
        if (characterError) {
          console.error('Error:', characterError);
        } else {
          const character = JSON.parse(characterBody);
          console.log(character.name);
        }
      });
    });
  }
});
