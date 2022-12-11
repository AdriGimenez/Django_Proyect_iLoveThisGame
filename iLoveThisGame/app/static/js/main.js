const form = document.getElementById("formulario");

form.addEventListener("submit", e=>{
     e.preventDefault()
     const email = document.getElementById("id_email");
     const nombre = document.getElementById("id_nombre");
     const apellido = document.getElementById("id_apellido");
     const telefono = document.getElementById("id_telefono");
     const parrafo = document.getElementById("warnings");

     let warnings = ""
     let entrar = false
     let regexEmail = /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/
     let regexTelefono = /^\d{7,14}$/
     parrafo.innerHTML = ""
    
     if(nombre.value.length <6){
         warnings += `El nombre no es valido <br>`
         entrar = true
     }
     if(!regexEmail.test(email.value)){
         warnings += `El email no es valido <br>`
         entrar = true
     }
     if(!regexTelefono.test(telefono.value)){
         warnings += `El telefono es invalido <br>`
         entrar = true
     }
     if(entrar){
         parrafo.innerHTML = warnings
    }else{
        parrafo.innerHTML = "Tu comentario fue enviado exitosamente!"
    }
})




