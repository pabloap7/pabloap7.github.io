function mostrarAutor() {
    var padre = document.getElementById("autor");
    if (!padre.querySelector('p')) {
        var hijo = document.createElement("p");
        hijo.innerHTML = "Hecho por: Pablo Arriola Pérez";
        padre.appendChild(hijo);
    }
} 