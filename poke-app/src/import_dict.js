import fs from "fs";

var text = fs.readFileSync("./poke-app/src/pokemon_links.txt");
let pokemon_list = text.toString().split("\n");
let pokemon_dict = {};
for (let i = 0; i < pokemon_list.length; i++) {
    let item = pokemon_list[i].split(",");
    let key = item[0];
    let value = item[1];
    pokemon_dict[key] = value;
}
console.log(pokemon_dict);
export default pokemon_dict;

