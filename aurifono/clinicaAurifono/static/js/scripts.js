/* inicio base */
let arrow = document.querySelectorAll(".arrow");
for(var i = 0; i < arrow.length; i++){
arrow[i].addEventListener("click", (e)=>{
    let arrowParent = e.target.parentElement.parentElement;
    arrowParent.classList.toggle("showMenu");
});
}

let menuPrincipal = document.querySelector('.menu-principal');
let menuPrincipalBtn = document.querySelector('.bx-menu');
let sessaoHome = document.querySelector('.sessao-home');
let conteudo = document.querySelector('.paginas');
let footer = document.querySelector('.footer');
menuPrincipalBtn.addEventListener("click", ()=>{
    menuPrincipal.classList.toggle("close");
    sessaoHome.classList.toggle("close");
    conteudo.classList.toggle("close");
    footer.classList.toggle("close");
});
/* fim base */
/* inicio Buscar */

let btnexcluir = document.getElementById('btn-excluir');
btnexcluir.addEventListener("click", function(e){
    e.preventDefault();
    let excluirlink = jQuery(this).attr('href')
    let resposta = confirm('Tem certeza que deseja excluir esse registro?')
    if(resposta){
        window.location.href = excluirlink
    }
});

let buscaForm = document.querySelector('#busca-form')
let btnForm = document.querySelector('#btn-busca')
btnForm.addEventListener('click', function(){
    buscaForm.submit()
});
/* fim buscar */