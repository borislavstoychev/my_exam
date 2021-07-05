import Splide from '@splidejs/splide';


// Create and mount the thumbnails slider.
const secondarySlider = new Splide('#secondary-slider', {
    rewind: true,
    fixedWidth: 100,
    fixedHeight: 64,
    isNavigation: true,
    gap: 10,
    focus: 'center',
    pagination: false,
    cover: true,
    breakpoints: {
        '600': {
            fixedWidth: 66,
            fixedHeight: 40,
        }
    }
}).mount();

// Create the main slider.
const primarySlider = new Splide('#primary-slider', {
    type: 'fade',
    heightRatio: 0.5,
    pagination: false,
    arrows: false,
    cover: true,
});

// Set the thumbnails slider as a sync target and then call mount.
primarySlider.sync( secondarySlider ).mount();