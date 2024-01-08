import * as fs from 'fs';

var text = fs.readFileSync("./pokemon_links.txt");
let pokemon_list = text.toString().split("\n");
let pokemon_dict = {};
for (let i = 0; i < pokemon_list.length; i++) {
    let item = pokemon_list[i].split(":");
    let key = item[0];
    let value = item[1];
    pokemon_dict[key] = value;
}

export default pokemon_dict;
