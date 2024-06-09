document.getElementById('search_form').addEventListener('submit', function(event) {
    event.preventDefault();

    var form = event.target;
    var formData = new FormData(form);

    fetch(form.action, {
        method: form.method,
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.puuid) {
            localStorage.setItem('puuid', data.puuid);
            document.getElementById('game_name').value = ''
            document.getElementById('tag_line').value = ''
            window.location.href = '/home';
        }else{
            alert('Erro: ' + data.error);
        }
    })
    .catch(error => {
        console.error('Erro:', error);
    });
});