<script>
import { onMount } from 'svelte';
import  container_module  from './main.js';

let counter_1 = 0;
let counter_2 = 0;
let dunno_counter = 0;

function incrementCounter() {
  counter_1 += 1;
};

function incrementCounter2() {
  counter_2 += 1;
};

function increment_dunno_counter() {
  dunno_counter += 1;
}

let pokemon_1 = "bulbasaur";
let pokemon_2 = "charmander";

</script>

<main>

  <body>

    <header>
        <h1>Which would you rather have?</h1>
    </header>
<div class="pair-container">
    <div class="container-1" on:click={incrementCounter}>    
      <h2>{pokemon_1} {counter_1}</h2>
            <img src="https://via.placeholder.com/150" alt="Placeholder">
    </div>

    <div class="container-2" on:click={incrementCounter2}>
            <h2>{pokemon_2} {counter_2}</h2>
            <img src="https://via.placeholder.com/150" alt="Placeholder">
    </div>
</div>
<br>
    <div class="dunno_button" on:click={increment_dunno_counter} aria-roledescription="button">Don't know! {dunno_counter}
    </div>
</body>

</main>