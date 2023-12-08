function setupAutocomplete(input, data) {
  var results = input.nextElementSibling;

  input.addEventListener("input", function () {
    var inputValue = input.value.toLowerCase();
    results.innerHTML = "";
    results.style.display = "none";

    if (inputValue.length > 0) {
      var filteredData = data.filter(function (item) {
        return item.toLowerCase().includes(inputValue);
      });

      if (filteredData.length > 0) {
        results.style.display = "block";
      }

      filteredData.forEach(function (item) {
        var li = document.createElement("li");
        li.textContent = item;
        results.appendChild(li);

        li.addEventListener("click", function () {
          input.value = item;
          results.innerHTML = "";
          results.style.display = "none";
        });
      });
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

  // Variables

  var municipio = JSON.parse(document.getElementById('municipios_data').textContent);
  var sede = ["Anexa", "Principal"];
  var remitidoPor = [
    "Docente",
    "Asesor de Grupo",
    "Coordinador",
    "Rector",
    "Acudiente o Tutor",
    "Estudiante (Por otro estudiante)",
    "Motivación Personal",
    "Remisión de Comité",
    "Focalización y/ o Seguimiento de orientación escolar",
    "Gestores de inclusión",
  ];
  var posiblesMotivosDeAtencion = [
    "comportamientos agresivos",
    "Violencia intrafamiliar",
    "Posible hiper-actividad y énfasis",
    "Violencia sexual",
    "Violencia basada en genero",
    "Consumo de sustancia psicoactivas",
    "Ideación suicida",
    "Intento de suicidio",
    "Cuttin- autoflagelación",
    "Baja tolerancia a la frustración",
    "Dificultades- problemas cognitivos del aprendizaje",
    "Embarazos en adolescentes",
    "Dificultades del orden emocional",
    "Acoso escolar Físico",
    "Acoso escolar Psicológico",
    "Acoso escolar Verbal",
    "Orientación sexual",
    "Trastornos en conducta alimentaria",
    "Delitos, según la ley colombiana",
  ];
  var tipoDeAtencion = ["Individual", "Familiar", "Grupal"]
  var entidadPrestadoraDeSalud = [
  "MALLAMAS",
  "AIC",
  "ASMET SALUD",
  "SALUD VIDA",
  "EMSANAR",
  "SISBEN",
  "COOMEVA",
  "NUEVA EPS",
  "SOS",
  "COSMITET",
  "SANITAS"
];
  var estudiantes = ['Juan', 'Camilo']

  // Fin Variables
  var dataSets = [
    municipio,
    sede,
    remitidoPor,
    posiblesMotivosDeAtencion,
    tipoDeAtencion,
    entidadPrestadoraDeSalud,
    estudiantes,

  ];

  var autocompleteInputs = document.querySelectorAll(".autocomplete-input");
  autocompleteInputs.forEach(function (input, index) {
    setupAutocomplete(input, dataSets[index]);
  });
});

document.addEventListener("DOMContentLoaded", function () {
  
  // Variables de completado automático
  const nombreCompletoEstudiante = document.getElementById("nombreCompletoEstudiante");
  const tipoDocumentoEstudiante = document.getElementById("tipoDocumentoEstudiante");
  const numeroDocumentoEstudiante = document.getElementById("numeroDocumentoEstudiante");
  const epsEstudiante = document.getElementById("epsEstudiante");
  const fechaNacimientoEstudiante = document.getElementById("fechaNacimientoEstudiante");
  const lugarNacimientoEstudiante = document.getElementById("lugarNacimientoEstudiante");
  


  // Fin Variables de completado automático
})