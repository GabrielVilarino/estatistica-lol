function obterPUUID() {
    return localStorage.getItem('puuid');
}
function mostrarPUUID() {
    let puuid = obterPUUID();
    if (puuid) {
        document.getElementById('puuid_placeholder').innerText = 'PUUID: ' + puuid;
    } else {
        alert(puuid)
        document.getElementById('puuid_placeholder').innerText = 'PUUID não encontrado';
    }
}