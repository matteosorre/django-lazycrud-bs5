function lazycrud_form_init() {
    var lang = document.documentElement.lang || 'default';
    var locale = (flatpickr.l10ns && flatpickr.l10ns[lang]) || flatpickr.l10ns.default;

    document.querySelectorAll('.dateinput').forEach(function(el) {
        flatpickr(el, {
            locale: locale,
            dateFormat: 'Y-m-d',
            altInput: true,
            altFormat: locale.dateFormat || 'Y-m-d',
            allowInput: true,
        });
    });
    document.querySelectorAll('.timeinput').forEach(function(el) {
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
    document.querySelectorAll('.datetimeinput').forEach(function(el) {
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

document.addEventListener('DOMContentLoaded', lazycrud_form_init);
