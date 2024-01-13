<script>
import { enhance } from '$app/forms';


let left_pokemon = 'charmander';
let right_pokemon = 'bulbasaur';
let who_won = 1;

</script>
<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>

<form action='?/uploadResult&left={left_pokemon}&right={right_pokemon}&winner={who_won}' method=POST use:enhance>

<button class = "btn btn-primary">Click me</button>
 
</form>



