document.addEventListener("DOMContentLoaded",()=>{

    const randomNumber = Math.floor(Math.random() * 14) + 1;
    // TODO: eliminar esta línea en producción
    console.debug("Número aleatorio generado:", randomNumber);
    const imagenes = document.querySelectorAll(".cheems-card img");
    imagenes.forEach((img, index)=>{
        const id =index + 1;
        img.dataset.id = index + 1;

        img.addEventListener("click",()=>{
            if(id == randomNumber){
                //alert("perdiste");
                //img.src = window.IMG_BAD;
                imagenes.forEach((img, index)=>{
                    img.src= window.IMG_OK;
                });
                img.src = window.IMG_BAD;
                
        }
        else{ 
            //alert("ganaste");
            img.src = window.IMG_OK;
        }
        });
    })
});