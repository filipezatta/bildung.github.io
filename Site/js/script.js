

var mensagens = document.getElementById("mensagens"); //ul
var caixatexto = document.getElementById("textbox");
var submit = document.getElementById("submit");
var avatar = document.getElementById("trocador");
var perfil = document.getElementById("perfil");
var imguser = "";
var nomeuser = "";



submit.addEventListener("click", function(){
    var horario = new Date().toLocaleTimeString();
    if(caixatexto.value == "avatar"){
        avatarchanger();
        caixatexto.value="";
        return;
    }
    if(imguser == ""){ 
        alert("Escolhe um user/avatar");
        return;
    };
    if(caixatexto.value == ""){
        alert("Escreve algo")
        return;
    }

    var novamensagem = document.createElement("li");
    var conteudomsg = `
    
    <div class="msgTelaGeral">
                        
    <img src="img/${imguser}.png"> 
    <span>${nomeuser}</span> 
    <span>${horario}</span>
    <div id="conteudomsg" class="conteudomsg">
        <span>${caixatexto.value}</span>
    </div>
    </div>
    `;
    novamensagem.innerHTML = conteudomsg;
    mensagens.appendChild(novamensagem);
    caixatexto.value="";
    mensagens.scrollIntoView(false);
});
function avatarchanger(){
    imguser = prompt("qual o teu avatar?");
    switch(imguser){
        case "lua":
            nomeuser = "Ben Duerr"
            break;
        case "dpedro":
            nomeuser = "Anão Rei";
            break;
        case "CU-1":
            nomeuser = "Varm Frågade"
            break;
        case "inor":
            nomeuser = "Dane Evans"
            break;        
    };
    avatarupdater()
    //alert(imguser);
}
var temperfil = 0;

function avatarupdater(){
    if(imguser ==""){
        return;
    }
    if(temperfil == 1){
        perfil.childNode.removeChild();

    };
    var novoperfil = document.createElement("div");
    var conteudoperfil = 
    `
    <div class="conteudoperfil">
        <span>${nomeuser}</span>           
        <img src="img/${imguser}.png"> 
    </div>
    `;
    novoperfil.innerHTML = conteudoperfil;
    perfil.appendChild(novoperfil);
    
    temperfil++

}


avatar.addEventListener("click", avatarchanger)

