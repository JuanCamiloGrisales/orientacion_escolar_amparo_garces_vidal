(function () {
    var beforePrint = function () {
      // Ocultar todos los elementos con la clase 'no-print'
      var elements = document.querySelectorAll('.no-print');
      elements.forEach(function (element) {
        element.style.display = 'none';
      });
      var containers = document.querySelectorAll('.container');
      containers.forEach(function (container) {
        container.style.width = '100vw';
        container.style.padding = '0';
        container.style.margin = '0';
      });
      var cards = document.querySelectorAll('.card');
      cards.forEach(function (card) {
        card.style.width = '100vw';
        card.style.padding = '0';
        card.style.margin = '0';
      });
      
    };

    var afterPrint = function () {
      // Mostrar todos los elementos con la clase 'no-print' de nuevo
      var elements = document.querySelectorAll('.no-print');
      elements.forEach(function (element) {
        element.style.display = ''; // Vaciar el estilo de display para volver al valor por defecto
      });
      var containers = document.querySelectorAll('.container');
      containers.forEach(function (container) {
        container.style.width = '';
        container.style.padding = '';
        container.style.margin = '';
      })
      var cards = document.querySelectorAll('.card');
      cards.forEach(function (card) {
        card.style.width = '';
        card.style.padding = '';
        card.style.margin = '';
      });
    };

    // Agregar listeners para los eventos de imprimir
    if (window.matchMedia) {
      var mediaQueryList = window.matchMedia('print');
      mediaQueryList.addListener(function (mql) {
        if (mql.matches) {
          beforePrint();
        } else {
          afterPrint();
        }
      });
    }

    // Listener para cubrir Internet Explorer
    window.onbeforeprint = beforePrint;
    window.onafterprint = afterPrint;
  })();