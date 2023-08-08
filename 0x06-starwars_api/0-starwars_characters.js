#!/usr/bin/node

const request = require('request');

function fetchCharacterName(characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
        return;
      }

      const characterData = JSON.parse(body);
      resolve(characterData.name);
    });
  });
}

function printMovieCharacters(movieId) {
  const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

  request(apiUrl, async (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }

    const filmData = JSON.parse(body);
    const characters = filmData.characters;

    for (const characterUrl of characters) {
      try {
        const characterName = await fetchCharacterName(characterUrl);
        console.log(characterName);
      } catch (error) {
        console.error(error);
      }
    }
  });
}

const movieId = process.argv[2];
if (movieId) {
  printMovieCharacters(movieId);
} else {
  console.log('Usage: ./0-starwars_characters.js <movie_id>');
}
