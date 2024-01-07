<script>
import { onMount } from 'svelte';

let pokemon_list = ['Eevee ♂', 'Pikachu ♀', 'Dragonite (?)', 'Bulbasaur ♀', 'Vaporeon ♂'];
let pokemon_imgs = {'Eevee ♂': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png',
                    'Pikachu ♀': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png',
                    'Dragonite (?)': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/149.png',
                    'Bulbasaur ♀': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png',
                    'Vaporeon ♂': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/134.png'};

// function to send data to the server and get a response
async function send_data_to_server(data) {
  const response = await fetch('http://localhost:5000/pokemon', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  });

  const json = await response.json();
  return json;
}

let pokemon_1 = "bulbasaur";
let pokemon_2 = "charmander";
let pokemon_img_1 = pokemon_imgs[pokemon_1];
let pokemon_img_2 = pokemon_imgs[pokemon_2];


let counter_1 = 0;
let counter_2 = 0;
let dunno_counter = 0;
var last_result = {pokemon_1: 'none', pokemon_2: 'none'};
var last_result_list = '';

function one_wins() {
  let results = {pokemon_1: 'winner', pokemon_2: 'loser'};
  // send_data_to_server(results);
  next_pokemon();
  last_result = results;
  last_result_list = pokemon_1+ " beats " + pokemon_2;
}

function two_wins() {
  let results = {pokemon_1: 'loser', pokemon_2: 'winner'};
  // send_data_to_server(results);
  next_pokemon();
  last_result = results;
  last_result_list = pokemon_2+ " beats " + pokemon_1;
} 

function draw() {
  let results = {pokemon_1: 'draw', pokemon_2: 'draw'};
  // send_data_to_server(results);
  next_pokemon();
  last_result = results;
  last_result_list = pokemon_1 + " drew against " + pokemon_2;
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
            <img src={pokemon_img_1} alt="Placeholder">
    </div>

    <div class="container-2" on:click={two_wins}>
            <h2>{pokemon_2}</h2>
            <img src={pokemon_img_2} alt="Placeholder">
    </div>
</div>
<br>
    <div class="dunno_button" on:click={draw} aria-roledescription="button">Don't know! <br> <br> Last result was: <br> {last_result_list}
    </div>
</body>

</main>