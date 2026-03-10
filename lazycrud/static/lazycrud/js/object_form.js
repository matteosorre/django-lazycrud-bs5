function lazycrud_form_init(form_id) {
    var lang = document.documentElement.lang || 'default';
    var locale = (flatpickr.l10ns && flatpickr.l10ns[lang]) || flatpickr.l10ns.default;

    var container = document.querySelector(form_id);
    if (!container) return;

    container.querySelectorAll('.dateinput').forEach(function(el) {
        flatpickr(el, { locale: locale, dateFormat: 'Y-m-d', allowInput: true });
    });
    container.querySelectorAll('.timeinput').forEach(function(el) {
        flatpickr(el, {
            locale: locale,
            enableTime: true,
            noCalendar: true,
            dateFormat: 'H:i',
            time_24hr: true,
            minuteIncrement: 15,
            allowInput: true,
        });
    });
    container.querySelectorAll('.datetimeinput').forEach(function(el) {
        flatpickr(el, {
            locale: locale,
            enableTime: true,
            dateFormat: 'Y-m-d H:i',
            time_24hr: true,
            minuteIncrement: 15,
            allowInput: true,
        });
    });
}

document.addEventListener('DOMContentLoaded', function() {
    lazycrud_form_init('form');
});
