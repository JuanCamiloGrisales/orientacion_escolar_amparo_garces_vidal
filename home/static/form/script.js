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
  var lineaDeAtencion = ["Orientación", "Prevención", "Intervención"]
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
    "SANITAS",
  ];
  var alumnosData = JSON.parse(document.getElementById('alumnos').textContent);
  var estudiantes = [];
  
  for (var nombreCompleto in alumnosData) {
    if (alumnosData.hasOwnProperty(nombreCompleto)) {
      estudiantes.push(nombreCompleto);
    }
  }

  // --------------------
  var sexo = ["Otro", "Mujer", "Hombre",];
  var genero = ["Otro", "Masculino", "Femenino"];
  var parentesco = [
    "Padre",
    "Madre",
    "Tio o Tia",
    "Abuelo o Abuela Paterna",
    "Abuelo o Abuela Materna",
    "Filia Política",
    "Pareja",
  ];
  var ocupacion = [
    "Agricultor",
    "Conductor",
    "Docente",
    "Ama de Casa",
    "Jornalero",
    "Empresario",
    "Independiente",
    "Comerciante",
  ];

  var nivelEducativo = [
    "No sabe no responde",
    "No estudió",
    "Primaria",
    "Secundaria",
    "Bachiller",
    "Técnico",
    "Tecnólogo",
    "Pregrado o Profesional",
    "Postgrado",
    "Doctorado",
  ];

  var estadoCivil = [
    "No sabe no responde",
    "Soltero",
    "Casado",
    "Divorciado",
    "Viudo",
    "Separado",
    "Unión Libre",
    "Comprometido",
    "N/A",
  ];

  var tipoDeFamilia = [
    "nuclear / heteroparental",
    "monoparental",
    "reconstituida",
    "extensa",
    "ensamblada",
    "familia de acogida",
    "adoptiva",
    "biparental",
    "homoparental",
    "Inmigrante",
    "Transnacional",
  ];

  // -----------------------
  var condicionDeDiscapacidad = [
    "No",
    "Si",
  ]

  var TipoDeDiscapacidad = [
    "Sensorial",
    "Intelectual",
    "Física",
    "Mental / Psicosocial",
  ]

  var talentoYCapacidadesExepcionales = [
    "Talento científico",
    "Talento Tecnológico",
    "Talento Atlético Deportivo",
    "Doble excepcionalidad",
    "Talento subjetivo artístico"
  ];

  var RemitidoA = [
    "Sí",
    "No remitido",
    "Coordinación de convivencia (Protocolo de Atención)",
    "Sector salud (Médico general, Fonoaudiología, Psicología)",
    "Sector protección (Comisaria de familia, ICBF, Policía de Infancia y adolescencia)",
    "Ministerio Público (personería, defensoría del pueblo, procuraduría, UARIV)",
    "Sector Justicia (fiscalía, policía)",
    "Comité de convivencia escolar",
    "Consejo directivo",
    "Consejo académico",
    "Seguimiento de orientación",
    "Atención de necesidades diversas de aprendizaje (PIAR)",
  ];

  var estadoDelCaso = ["Abierto", "Cerrado"];

  // Fin Variables
  var dataSets = [
    municipio,
    sede,
    remitidoPor,
    posiblesMotivosDeAtencion,
    lineaDeAtencion,
    tipoDeAtencion,
    entidadPrestadoraDeSalud,
    estudiantes,
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
    RemitidoA,
    estadoDelCaso

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
  const lugarNacimientoEstudiante = document.getElementById("lugarNacimientoEstudiante");
  const direccion = document.getElementById("direccion");

  // Input:
  var inputNombreEstudiante = document.getElementById("nombreEstudiante");

  
  function autocompleter() {
      Valor = inputNombreEstudiante.value;
      
      if (alumnosData.hasOwnProperty(Valor)) {
        tipoDocumentoEstudiante.value = alumnosData[Valor].tipo_documento;
        numeroDocumentoEstudiante.value = alumnosData[Valor].numero_documento;
        epsEstudiante.value = alumnosData[Valor].eps;
        fechaNacimientoEstudiante.value = alumnosData[Valor].fecha_nacimiento;
        lugarNacimientoEstudiante.value = alumnosData[Valor].lugar_nacimiento;
        direccion.value = alumnosData[Valor].barrio;
      } else {
        tipoDocumentoEstudiante.value = "";
        numeroDocumentoEstudiante.value = "";
        epsEstudiante.value = "";
        fechaNacimientoEstudiante.value = "";
        lugarNacimientoEstudiante.value = "";
        direccion.value = "";
      }
    }

  inputNombreEstudiante.addEventListener("input", autocompleter);
  inputNombreEstudiante.addEventListener("change", autocompleter);
  inputNombreEstudiante.addEventListener("click", autocompleter);
  inputNombreEstudiante.addEventListener("keyup", autocompleter);
    
  


  // Fin Variables de completado automático
})


// Código para archivos multiples
document.addEventListener("DOMContentLoaded", function () {
  const filesInput = document.getElementById('files');
  const preview = document.getElementById('preview');
  const form = document.getElementById('uploadForm');

  filesInput.addEventListener('change', function (event) {
    preview.innerHTML = '';
    for (let i = 0; i < filesInput.files.length; i++) {
      let file = filesInput.files[i];
      let fileDiv = document.createElement('div');
      fileDiv.textContent = file.name;
      fileDiv.className = 'mb-2';
      let deleteButton = document.createElement('button');
      deleteButton.textContent = 'Eliminar';
      deleteButton.className = 'btn text-white btn-sm ms-2';
      deleteButton.onclick = function () {
        // Eliminar el archivo del input.
        let newFileList = Array.from(filesInput.files).filter(function (f) {
          return f.name !== file.name;
        });
        filesInput.files = new DataTransfer().files;
        newFileList.forEach(function (f) {
          let dt = new DataTransfer();
          dt.items.add(f);
          filesInput.files = dt.files;
        });
        // Eliminar la vista previa del archivo.
        fileDiv.remove();
      };
      fileDiv.appendChild(deleteButton);
      preview.appendChild(fileDiv);
    }
  });

  // form.addEventListener('submit', function (event) {
  //   event.preventDefault();
  //   // Aquí podrías usar FormData para enviar los archivos a Django con AJAX.
  //   let formData = new FormData(form);
  //   // Ejemplo de cómo enviar los datos usando fetch.
  //   fetch('/upload/', {
  //     method: 'POST',
  //     body: formData,
  //   })
  //   .then(response => response.json())
  //   .then(data => console.log(data))
  //   .catch(error => console.error(error));
  // });
});