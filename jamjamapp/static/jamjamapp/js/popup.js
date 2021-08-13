function showPopup(multipleFilter) {
	const popup = document.querySelector('#popup');
  
  if (multipleFilter) {
  	popup.classList.add('multiple-filter');
  } else {
  	popup.classList.remove('multiple-filter');
  }
  
  popup.classList.remove('hide');
}

function closePopup() {
	const popup = document.querySelector('#popup');
  popup.classList.add('hide');
}