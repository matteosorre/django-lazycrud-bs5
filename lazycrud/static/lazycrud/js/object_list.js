document.addEventListener('DOMContentLoaded', function () {
    document.body.addEventListener('mousedown', function (e) {
        var row = e.target.closest('.clickable_row');
        if (!row) return;
        if (e.target.closest('a, button')) return;  // permette di cliccare su buttons sulla riga
        var url = row.dataset.url;
        if (!url) return;
        if (row.dataset.target === '_blank' || e.button === 2) {
            window.open(url);
        } else {
            window.location.href = url;
        }
    });
});
