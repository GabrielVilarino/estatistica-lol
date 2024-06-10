/*
Autor: Gabriel Vilarino

Script da página inicial
*/

function obterNome() {
    /*
    Obtém o nome e a tag do jogador
    */
    let storedData = localStorage.getItem('userData');
    let parsedData = JSON.parse(storedData);

    let nomeJogador = parsedData.data.gameName;
    let tagJogador = `#${parsedData.data.tagLine}`;

    let invocador = nomeJogador + tagJogador
    
    document.getElementById('nome_jogador').textContent = invocador;
}

function obterIcone() {
    fetch('/obter-icone')
        .then(response => response.json())
        .then(data => {

            if (data.idIcone) {
                let urlIcone = `https://ddragon.leagueoflegends.com/cdn/14.11.1/img/profileicon/${data.idIcone}.png`;
                icone = document.getElementById('icone_jogador');
                icone.src = urlIcone
            } else {
                console.error('Erro na requisição:', data.error);
            }
        })
        .catch(error => {
            console.error('Erro ao obter ícone:', error);
        });
}

document.addEventListener('DOMContentLoaded', function() {
    obterNome()
    obterIcone()
});