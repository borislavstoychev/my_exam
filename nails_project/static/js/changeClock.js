const imageSources = [
    'static/images/clock.svg',
    'static/images/clock1.svg',
    'static/images/clock2.svg',
    'static/images/clock3.svg',
    'static/images/clock4.svg',
    'static/images/clock5.svg',
    'static/images/clock6.svg',
]

let index = 0;
setInterval(function () {
    if (index === imageSources.length) {
        index = 0;
    }
    document.getElementById("image-clock").src = imageSources[index];
    index++;
}, 2000);