import fs from "fs";

var text = fs.readFileSync("./individual_pokemon.txt");
let pokemon_list = text.toString().split("\n");

export default pokemon_list;

