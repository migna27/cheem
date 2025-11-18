document.addEventListener("DOMContentLoaded",()=>{

    const randomNumber = Math.floor(Math.random() * 14) + 1;
    // TODO: eliminar esta línea en producción
    console.debug("Número aleatorio generado:", randomNumber);
    const imagenes = document.querySelectorAll(".cheems-card img");

    
    const clickedCards = new Set();

    imagenes.forEach((img, index) => {
        const id = index + 1;
        img.dataset.id = index + 1;

        
        img.addEventListener("click", () => {
            
            if (!clickedCards.has(id)) {
                
                clickedCards.add(id);
            }

            if (id === randomNumber) {
              
                imagenes.forEach((img, index) => {
                    img.src = window.IMG_OK;
                });
                
                img.src = window.IMG_BAD;
                alert("¡Perdiste! Has pulsado la imagen incorrecta.");
            } else {
                
                img.src = window.IMG_OK;

                
                if (clickedCards.size === 14) {
                    //alert("¡Ganaste! Has encontrado todas las imágenes correctas.");
                    const modal = new bootstrap.Modal(document.getElementById('modal-winner'));
                    modal.show();
                }
            }
        });
    });
});