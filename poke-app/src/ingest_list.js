import fs from "fs";

var text = fs.readFileSync("./poke-app/src/individual_pokemon.txt");
let pokemon_list = text.toString().split("\n");


console.log(pokemon_list);

export default pokemon_list;

