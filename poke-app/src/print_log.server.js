export function print_log () {
    console.log('print_log');
}


import { secret_text } from '../lib/server/secrets.js';

console.log(secret_text);