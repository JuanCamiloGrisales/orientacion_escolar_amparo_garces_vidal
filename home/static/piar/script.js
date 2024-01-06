function setupAutocomplete(input, data) {
  var results = input.nextElementSibling;

  const resultados = () => {
    var inputValue = input.value.toLowerCase();
    results.innerHTML = "";
    results.style.display = "none";

    var filteredData = data.filter(function (item) {
      return inputValue.length === 0 || item.toLowerCase().includes(inputValue);
    });

    if (filteredData.length > 0) {
      results.style.display = "block";
    }

    filteredData.forEach(function (item) {
      var li = document.createElement("li");
      li.textContent = item;
      li.style.zIndex = "9999"; // Un valor muy alto
      results.appendChild(li);

      li.addEventListener("click", function () {
        input.value = item;
        results.innerHTML = "";
        results.style.display = "none";
      });
    });
  };

  input.addEventListener("input", resultados);

  // Se modifica el evento de "click" para que no dependa del contenido del input
  input.addEventListener("click", function (event) {
    if (input.value === "") {
      resultados();
    }
  });

  input.addEventListener("keydown", function (e) {
    if (e.keyCode === 9 && results.firstChild) {
      // Tab key
      e.preventDefault();
      input.value = results.firstChild.textContent;
      results.innerHTML = "";
      results.style.display = "none";
    }
  });

  document.addEventListener("click", function (e) {
    if (e.target !== input) {
      results.innerHTML = "";
      results.style.display = "none";
    }
  });
}

document.addEventListener("DOMContentLoaded", function () {
  var alumnosData = JSON.parse(document.getElementById("alumnos").textContent);
  var estudiantes = [];

  for (var nombreCompleto in alumnosData) {
    if (alumnosData.hasOwnProperty(nombreCompleto)) {
      estudiantes.push(nombreCompleto);
    }
  }

  var dataSets = [estudiantes];

  var autocompleteInputs = document.querySelectorAll(".autocomplete-input");
  autocompleteInputs.forEach(function (input, index) {
    setupAutocomplete(input, dataSets[index]);
  });
});
