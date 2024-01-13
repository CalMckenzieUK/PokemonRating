import type { Actions } from "@sveltejs/kit";
import { query } from "../lib/server/db_interaction.js";

export const actions: Actions = {
    uploadResult: async (request) => {
      let split_url = request.url.href.split("?")[1].split("&");
      console.log(split_url);
      const left_pokemon_name = split_url[2].split("=")[1];
      const right_pokemon_name = split_url[1].split("=")[1];
      const who_won = split_url[0].split("=")[1];
      console.log(left_pokemon_name, right_pokemon_name, who_won);
      query(`insert into pokemon_rating (left_pokemon_name, right_pokemon_name, who_won) values ("${left_pokemon_name}","${right_pokemon_name}","${who_won}")`);
      return {
        body: {
          left_pokemon_name,
          right_pokemon_name,
          who_won
        }
      };
}}

