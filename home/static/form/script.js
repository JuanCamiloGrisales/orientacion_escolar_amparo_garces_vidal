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
  input.addEventListener("click", function(event) {
    if (input.value === '') {
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

  // Variables

  var municipio = JSON.parse(document.getElementById('municipios_data').textContent);
  var institucion = JSON.parse(document.getElementById('institucion_data').textContent);
  var dane = JSON.parse(document.getElementById('dane_data').textContent);
  var sede = JSON.parse(document.getElementById('sede_data').textContent);;
  var remitidoPor = JSON.parse(document.getElementById('remitidoPor_data').textContent);
  var nombreRemitidoPor = JSON.parse(document.getElementById('nombreRemitidoPor_data').textContent);
  var posiblesMotivosDeAtencion = JSON.parse(document.getElementById('posiblesMotivosDeAtencion_data').textContent);
  var lineaDeAtencion = JSON.parse(document.getElementById('lineaDeAtencion_data').textContent);
  var tipoDeAtencion = JSON.parse(document.getElementById('tipoDeAtencion_data').textContent);
  var entidadPrestadoraDeSalud = JSON.parse(document.getElementById('entidadPrestadoraDeSalud_data').textContent);
  var alumnosData = JSON.parse(document.getElementById('alumnos').textContent);
  var estudiantes = [];
  
  for (var nombreCompleto in alumnosData) {
    if (alumnosData.hasOwnProperty(nombreCompleto)) {
      estudiantes.push(nombreCompleto);
    }
  }

  tipoDocumentoEstudianteDatos = JSON.parse(document.getElementById('tipoDocumentoEstudiante_data').textContent);
  gradoEscolaridad = JSON.parse(document.getElementById('gradoEscolaridad_data').textContent);

  // --------------------
  var sexo = JSON.parse(document.getElementById('sexo_data').textContent);
  var genero = JSON.parse(document.getElementById('genero_data').textContent);
  var parentesco = JSON.parse(document.getElementById('parentesco_data').textContent);
  var ocupacion = JSON.parse(document.getElementById('ocupacion_data').textContent);

  var nivelEducativo = JSON.parse(document.getElementById('nivelEducativo_data').textContent);

  var estadoCivil = JSON.parse(document.getElementById('estadoCivil_data').textContent);

  var tipoDeFamilia = JSON.parse(document.getElementById('tipoFamilia_data').textContent);

  // -----------------------
  var condicionDeDiscapacidad = JSON.parse(document.getElementById('condicionDiscapacidad_data').textContent);

  var TipoDeDiscapacidad = JSON.parse(document.getElementById('tipoDiscapacidad_data').textContent);
  var talentoYCapacidadesExepcionales = JSON.parse(document.getElementById('talentoYCapacidadesExepcionales_data').textContent);

  var activacionRuta = JSON.parse(document.getElementById('activacionRuta_data').textContent);

  var estadoCaso = JSON.parse(document.getElementById('estadoCaso_data').textContent);
  var nombreOrientadora = JSON.parse(document.getElementById('nombreOrientadora_data').textContent);

  // Fin Variables
  var dataSets = [
    municipio,
    institucion,
    dane,
    sede,
    remitidoPor,
    nombreRemitidoPor,
    posiblesMotivosDeAtencion,
    lineaDeAtencion,
    tipoDeAtencion,
    entidadPrestadoraDeSalud,
    estudiantes,
    tipoDocumentoEstudianteDatos,
    gradoEscolaridad,
    entidadPrestadoraDeSalud,
    municipio,
    sexo,
    genero,
    parentesco,
    ocupacion,
    nivelEducativo,
    estadoCivil,
    tipoDeFamilia,
    condicionDeDiscapacidad,
    TipoDeDiscapacidad,
    talentoYCapacidadesExepcionales,
    activacionRuta,
    estadoCaso,
    nombreOrientadora

  ];

  var autocompleteInputs = document.querySelectorAll(".autocomplete-input");
  autocompleteInputs.forEach(function (input, index) {
    setupAutocomplete(input, dataSets[index]);
  });
});

document.addEventListener("DOMContentLoaded", function () {
  
  var alumnosData = JSON.parse(document.getElementById('alumnos').textContent);

  // Variables de completado automático
  const tipoDocumentoEstudiante = document.getElementById("tipoDocumentoEstudiante");
  const numeroDocumentoEstudiante = document.getElementById("numeroDocumentoEstudiante");
  const epsEstudiante = document.getElementById("epsEstudiante");
  const fechaNacimientoEstudiante = document.getElementById("fechaNacimientoEstudiante");
  const direccion = document.getElementById("direccion");
  const gradoEscolaridad = document.getElementById("gradoEscolaridad");

  // Input:
  var inputNombreEstudiante = document.getElementById("nombreEstudiante");

  
function autocompleter() {
    const Valor = inputNombreEstudiante.value;
    const alumno = alumnosData[Valor] || {};

    tipoDocumentoEstudiante.value = alumno.tipo_documento || "";
    numeroDocumentoEstudiante.value = alumno.numero_documento || "";
    epsEstudiante.value = alumno.eps || "";
    fechaNacimientoEstudiante.value = alumno.fecha_nacimiento || "";
    direccion.value = alumno.barrio || "";
    gradoEscolaridad.value = alumno.grado_escolaridad || "";
}

  inputNombreEstudiante.addEventListener("input", autocompleter);
  inputNombreEstudiante.addEventListener("change", autocompleter);
  inputNombreEstudiante.addEventListener("click", autocompleter);
  inputNombreEstudiante.addEventListener("keyup", autocompleter);

  // Fin Variables de completado automático
})

function llenarFormularioConJson(jsonData, formularioId) {
  // Obtener el formulario por su ID
  var formulario = document.getElementById(formularioId);

  // Verificar si el formulario y los datos están presentes
  if (formulario && jsonData) {
    // Iterar sobre las claves del JSON
    for (var clave in jsonData) {
      if (jsonData.hasOwnProperty(clave)) {
        // Excluir el campo csrf_token
        if (clave === 'csrfmiddlewaretoken') {
          continue;
        }

        // Obtener el elemento de formulario por su nombre
        var elemento = formulario.elements[clave];

        // Verificar si el elemento existe en el formulario
        if (elemento) {
          // Establecer el valor del elemento con el valor correspondiente del JSON
          elemento.value = jsonData[clave];
        }
      }
    }
  } else {
    console.error("Formulario o datos no encontrados.");
  }
}