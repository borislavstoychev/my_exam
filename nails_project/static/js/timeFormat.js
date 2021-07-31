const timepicker = new TimePicker('time', {
  lang: 'en',
  theme: 'dark'
});
timepicker.on('change', function(evt) {

  const value = (evt.hour || '00') + ':' + (evt.minute || '00');
  evt.element.value = value;

});