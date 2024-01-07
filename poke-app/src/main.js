import './styles.css'
import App from './App.svelte'

const app = new App({
  target: document.getElementById('app'),
})

export default app

// Define the dictionary of elements
const elements = {
  container1: ['element1', 'element2', 'element3'],
  container2: ['element4', 'element5', 'element6']
};

// Define the module
const containerModule = (() => {
  let previousValues = {};

  // Function to handle click events
  const handleClick = (container) => {
      // Save the previous value
      previousValues[container] = document.getElementById(container).innerText;

      // Select a new element from the dictionary
      const newElement = elements[container][Math.floor(Math.random() * elements[container].length)];

      // Update the value of the container
      document.getElementById(container).innerText = newElement;

      // Return the new value
      return newElement;
  };

  // Function to initialize the module
  const init = () => {
      // Add click event listeners to the containers
      document.getElementById('container-1').addEventListener('click', () => handleClick('container-1'));
      document.getElementById('container-2').addEventListener('click', () => handleClick('container-2'));
  };

  // Return the public methods
  return {
      init
  };
})();

// Initialize the module
containerModule.init();
