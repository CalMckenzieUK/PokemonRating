<script>
    import dict from '../lib/dict.js';
    import list from '../lib/list.js'; 
    import info from '../lib/pokemon_obtainability_list.js' 
    import rarity from '../lib/rarity.js'
    
    let url_start = "?/uploadResult&left="

    let pokemon_obtainability = info;
    let pokemon_imgs = dict;
    let pokemon_list = list;
    let pokemon_rarity = rarity;
    let quantity_var = "";
    let gender_var = "";
    let gender_disc = "";

    
    let pokemon_1 = "";
    let pokemon_2 = "";
    let pokemon_1_no_gender = "";
    let pokemon_2_no_gender = "";
  

    let pokemon_img_1 = "https://wiki.p-insurgence.com/images/0/09/722.png";
    let pokemon_img_2 = "https://wiki.p-insurgence.com/images/0/09/722.png";
    
    var last_result = {pokemon_1: 'none', pokemon_2: 'none'};
    var last_result_list = "Click a MissingNo to start...";
    
    function one_wins() {
      let results = {pokemon_1: 'winner', pokemon_2: 'loser'};
      let winner = '1'
      
      last_result = results;
      if (pokemon_1 == "") {
        last_result_list = "Select a Pokemon and your latest choice will be shown here!";
      }
      else {

      var xhr = new XMLHttpRequest();
      xhr.open("POST", url_start.concat(pokemon_1,"&right=",pokemon_2,"&winner=",winner));
      xhr.send('lol')
      last_result_list = "Last result was: <br>" + pokemon_1+ " beats " + pokemon_2;}
      next_pokemon();
    }
    
    function two_wins() {
      let results = {pokemon_1: 'loser', pokemon_2: 'winner'};
      let winner = '2'
      last_result = results;
      if (pokemon_1 == "") {
        last_result_list = "Select a Pokemon and your latest choice will be shown here!";
      }
      else {
      var xhr = new XMLHttpRequest();
      xhr.open("POST", url_start.concat(pokemon_1,"&right=",pokemon_2,"&winner=",winner));
      xhr.send('lol')
      last_result_list = "Last result was: <br>" +pokemon_2 + " beats " + pokemon_1;}
      next_pokemon();
    } 
    
    function draw() {
      let results = {pokemon_1: 'draw', pokemon_2: 'draw'};
      let winner = '0'
      last_result = results;
      if (pokemon_1 == "") {
        last_result_list = "Select a Pokemon and your latest choice will be shown here!";
      }
      else {
      var xhr = new XMLHttpRequest();
      xhr.open("POST", url_start.concat(pokemon_1,"&right=",pokemon_2,"&winner=",winner));
      xhr.send('lol');
      last_result_list = "Last result was: <br>" +pokemon_1 + " drew against " + pokemon_2;
      }
      next_pokemon();
    
    }
    
    function next_pokemon(){
      let new_one = pokemon_list[Math.floor(Math.random() * pokemon_list.length)];
      let new_two = pokemon_list[Math.floor(Math.random() * pokemon_list.length)]
      quantity_var = 'Quantity in game: '
      gender_var = 'Obtained by:'
      gender_disc = '(Obtainability info is NOT gender specific)'
      while (new_one == new_two){
        new_two = pokemon_list[Math.floor(Math.random() * pokemon_list.length)]
      }
      
      pokemon_1 = new_one;
      pokemon_2 = new_two;
      pokemon_img_1 = pokemon_imgs[pokemon_1];
      pokemon_img_2 = pokemon_imgs[pokemon_2];

      pokemon_1_no_gender = pokemon_1.replace(' M', '').replace(' F', '').replace(' U', '').replace(' G','')
      if (pokemon_1_no_gender.includes('Unown')) {
        pokemon_1_no_gender = pokemon_1_no_gender.replace(indexOf('Unown')+6, '')
      }

      pokemon_2_no_gender = pokemon_2.replace(' M', '').replace(' F', '').replace(' U', '').replace(' G','')
      if (pokemon_2_no_gender.includes('Unown')) {
        pokemon_2_no_gender = pokemon_2_no_gender.replace(indexOf('Unown')+6, '')
      }
      
      
    };

    </script>
   
   <style>


main {
    height: 80vh;
}
body {
    font-family: Verdana, Tahoma, sans-serif;
    font-size: max(18px, 18px);
    background-color: lightsteelblue;
    justify-content: center;
    text-align: center;
}
.pair-container {
    max-height: 60vh;
    display: grid;
    grid-template-columns: 1fr 1fr;
    flex-direction: column;
    width: 100%;
}
.container-1 {
    font-size: max(14px, 14px);
    max-height: 300px;
    max-width: 600px;
    text-wrap: wrap;
    text-align: center;
    padding-top: 0vw;
    margin-left: 8vw;
    height: 35vw;
    min-height: 280px;
    min-width: 200px;
    width: 30vw;
    background-color: paleturquoise;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);;
}
.container-2 {
    font-size: max(14px, 14px);
    max-height: 300px;
    max-width: 600px;
    text-align: center;
    padding-top: 0vw;
    margin-left: 5vw;
    margin-right: 5vw;
    height: 35vw;
    width: 30vw;
    min-height: 280px;
    min-width: 200px;
    background-color: paleturquoise;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
}
.container-1:hover {
    background-color: lightcyan;
    transform: rotate(-3deg) scale(1.05);
    transition: 0.2s ease-out;
}
.container-2:hover {
    background-color: lightcyan;
    transform: rotate(3deg) scale(1.05);
    transition: 0.2s ease-in-out;   
}
.dunno_button {
    font-size: max(16px, 16px);
    margin:auto;
    max-width: 450px;
    max-height: 20px;
    background-color: palegoldenrod;
    width: 50vw;
    height: 3vw;
    border-radius: 10px;
    font-weight: bold;
    color: black;
    padding: 15px 32px;
    text-align: center;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
}
.dunno_button:hover {
    background-color: lightgoldenrodyellow;
    transform: rotate(3deg) scale(1.05);
    transition: 0.2s ease-in-out;   
}
.image {
    max-width: max-content;
    max-height: max-content;
    border-radius: 10px;
    padding-top: 5px;

}
.previous_battle {
    font-size: max(10px, 16px);
    max-width: 900px;
    max-height: 90px;
    min-height: 80px;
    margin:auto;
    background-color: pink;
    width: 78vw;
    height: 10vw;
    border-radius: 10px;
    font-weight: bold;
    color: black;
    /* padding: 15px 15vw; */
    /* box-shadow: 0 2px 4px rgba(0, 0, 0, 0.5); */
}



   </style>
   
    <main>
      <body>
        <header draggable="false">
            <h1>Which would you rather have?</h1>
        </header>
        <p><b>{gender_disc}</b></p>
    <div class="pair-container">
      <form name='one_wins'>
    <div class="container-1" on:click={one_wins} draggable="false">    
      <h2>{pokemon_1}</h2>
                <img src={pokemon_img_1} class="image" alt="Placeholder" draggable="false">    
                <div class="info1" draggable="false">
                  <p>{quantity_var} <b>{rarity[pokemon_1]}</b></p>  
                  <!-- <p> {gender_var}</p>   -->
                  <p><i> {pokemon_obtainability[pokemon_1_no_gender]}</i> </p> 
                    
        </div>
    </form>
    <form name='two_wins'>
        <div class="container-2" on:click={two_wins} draggable="false">
                <h2>{pokemon_2}</h2>
                <img src={pokemon_img_2} class="image" alt="Placeholder" draggable="false">
                <div class="info2" draggable="false">
                  <p>{quantity_var} <b>{rarity[pokemon_2]}</b></p>
                  <!-- <p> {gender_var}</p>   -->
                  <p> <i>{pokemon_obtainability[pokemon_2_no_gender]} </i></p> 
        </div>
    </form>
    </div>
    <br>
    <form name='draw'>
        <div class="dunno_button" on:click={draw} aria-roledescription="button">Don't know! <br> <br> 
        </div>
    </form>
        <br>
        <div class="previous_battle"> <br> {@html last_result_list} </div>
        <br><br>

        <div class="elo_table">
            <embed src="https://pokemonrating-5vda68brbsp8jnobggqe9u.streamlit.app/?embedded=true" width="750px" height="500px" />

        </div>


    </body>
    </main>


    