(function () {
  var visor = document.querySelector(".visor");
  if (visor && visor.showModal) {
    var foto = visor.querySelector("img");
    document.addEventListener("click", function (e) {
      var enlace = e.target.closest("[data-ampliar]");
      if (!enlace) return;
      e.preventDefault();
      foto.src = enlace.href;
      foto.alt = (enlace.querySelector("img") || {}).alt || "";
      visor.showModal();
    });
    visor.addEventListener("click", function (e) { if (e.target === visor) visor.close(); });
  }

  var producto = new URLSearchParams(location.search).get("producto");
  var campo = document.querySelector('.formulario [name="producto"]');
  if (producto && campo) campo.value = producto;
})();
