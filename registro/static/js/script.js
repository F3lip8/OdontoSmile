let slideIndex = 0;

function showSlide(n) {
const slides = document.getElementsByClassName("slide");
if (n >= slides.length) {slideIndex = 0;}
if (n < 0) {slideIndex = slides.length
1;}
for (let i = 0; i < slides.length; i++) {
slides[i].style.display = "none";
}
slides[slideIndex].style.display = "block";
}
function nextSlide() {
showSlide(slideIndex += 1);
}

function prevSlide() {
    if (slideIndex === 0){
        showSlide(slideIndex = slides.length - 1);
        console.log(slides.length);
    }
    else {
        showSlide(slideIndex -= 1);
    }
}

showSlide(slideIndex);
