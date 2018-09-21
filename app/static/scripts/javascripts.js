function hidMessageDiv() {
    if (document.getElementById('message').style.display == 'block') {
        setTimeout(function() {
            document.getElementById('message').style.display = 'none';
        }, 10000);
    }
}