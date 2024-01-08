<script>
import { onMount } from 'svelte';
import pokemon_list  from './ingest_list';
import pokemon_dict from './import_dict';

// let pokemon_list = ['Eevee ♂', 'Pikachu ♀', 'Dragonite (?)', 'Bulbasaur ♀', 'Vaporeon ♂'];

let pokemon_imgs = pokemon_dict;


// let pokemon_imgs = {'Eevee ♂': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png',
//                     'Pikachu ♀': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png',
//                     'Dragonite (?)': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/149.png',
//                     'Bulbasaur ♀': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png',
//                     'Vaporeon ♂': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/134.png'};


let pokemon_1 = "";
let pokemon_2 = "";
let pokemon_img_1 = "https://wiki.p-insurgence.com/images/0/09/722.png";
let pokemon_img_2 = "https://wiki.p-insurgence.com/images/0/09/722.png";


let counter_1 = 0;
let counter_2 = 0;
let dunno_counter = 0;
var last_result = {pokemon_1: 'none', pokemon_2: 'none'};
var last_result_list = "Click a MissingNo to start...";

function one_wins() {
  let results = {pokemon_1: 'winner', pokemon_2: 'loser'};
  // send_data_to_server(results);
  last_result = results;
  if (pokemon_1 == "") {
    last_result_list = "Select a Pokemon and your latest choice will be shown here!";
  }
  else {
  last_result_list = "Last result was: <br>" + pokemon_1+ " beats " + pokemon_2;}
  next_pokemon();
}

function two_wins() {
  let results = {pokemon_1: 'loser', pokemon_2: 'winner'};
  // send_data_to_server(results);
  last_result = results;
  if (pokemon_1 == "") {
    last_result_list = "Select a Pokemon and your latest choice will be shown here!";
  }
  else {
  last_result_list = "Last result was: <br>" +pokemon_2 + " beats " + pokemon_1;}
  next_pokemon();
} 

function draw() {
  let results = {pokemon_1: 'draw', pokemon_2: 'draw'};
  // send_data_to_server(results);
  last_result = results;
  if (pokemon_1 == "") {
    last_result_list = "Select a Pokemon and your latest choice will be shown here!";
  }
  else {
  last_result_list = "Last result was: <br>" +pokemon_1 + " drew against " + pokemon_2;}
  next_pokemon();

}


function next_pokemon(){
  let new_one = pokemon_list[Math.floor(Math.random() * pokemon_list.length)];
  let new_two = pokemon_list[Math.floor(Math.random() * pokemon_list.length)]
  while (new_one == new_two){
    new_two = pokemon_list[Math.floor(Math.random() * pokemon_list.length)]
  }
  pokemon_1 = new_one;
  pokemon_2 = new_two;
  pokemon_img_1 = pokemon_imgs[pokemon_1];
  pokemon_img_2 = pokemon_imgs[pokemon_2];
};


function increment_dunno_counter() {
  dunno_counter += 1;
}


</script>

<main>

  <body>

    <header>
        <h1>Which would you rather have?</h1>
    </header>
<div class="pair-container">
    <div class="container-1" on:click={one_wins}>    
      <h2>{pokemon_1}</h2>
            <img src={pokemon_img_1} class="image" alt="Placeholder">
    </div>

    <div class="container-2" on:click={two_wins}>
            <h2>{pokemon_2}</h2>
            <img src={pokemon_img_2} class="image" alt="Placeholder">
    </div>
</div>
<br>
    <div class="dunno_button" on:click={draw} aria-roledescription="button">Don't know! <br> <br> 
    </div>
    <br>
    <div class="previous_battle"> <br> {@html last_result_list} </div>
</body>

</main>