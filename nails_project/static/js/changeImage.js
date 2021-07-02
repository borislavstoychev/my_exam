const imageSources = ['https://40plusstyle.com/wp-content/uploads/2013/07/nails1.jpg', "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F37%2F2021%2F03%2F10%2FSpring-fingernails.jpg"];

let index = 0;
setInterval(function () {
    if (index === imageSources.length) {
        index = 0;
    }
    document.getElementById("image").src = imageSources[index];
    index++;
}, 2000);

