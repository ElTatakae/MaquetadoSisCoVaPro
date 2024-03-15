
var slider = document.getElementById('inputObjetivoRange');
var output = document.getElementById('rangeValue');

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
  output.innerHTML = this.value;
}

// Call the function to display the initial value
slider.oninput();