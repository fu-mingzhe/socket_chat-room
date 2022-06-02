let img1 = document.querySelector('.img1');
let img2 = document.querySelector('.img2');
let resBox = document.querySelector('.res-box');
let numImg = document.createElement('img');
let h3 = document.querySelector('h3');
h3.classList.add('hide');
resBox.classList.add('hide');


setTimeout(() => {
		img1.classList.add('hide');
		resBox.appendChild(numImg);
		img2.classList.remove('hide');
		h3.classList.remove('hide');		
		resBox.classList.remove('hide');		
}, 2000);