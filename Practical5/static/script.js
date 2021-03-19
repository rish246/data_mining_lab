const ourForm = document.querySelector('form');

const submitButton = document.querySelector('button');

submitButton.addEventListener('submit', (e) => {
    e.preventDefault();
    console.log("The form has been submitted");
    ourForm.submit();
})