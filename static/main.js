const dropdown = document.querySelector("#firstBox");
const dropdownContent = document.getElementById("dropdownContent");
const form = document.getElementById('text-form');
const mealInput = document.getElementById('selectedMeal');
let selectedOption = null;

dropdownContent.addEventListener('mouseenter', function () {
    dropdown.style.borderRadius = '20px 0 0 0';
});

dropdownContent.addEventListener('mouseleave', function () {
    dropdown.style.borderRadius = ''; 
});

dropdownContent.addEventListener('click', function(event) {
  const selectedMeal = event.target.id;
  mealInput.value = selectedMeal;

  if (selectedOption) {
    selectedOption.style.backgroundColor = '';
  }

  event.target.style.backgroundColor = "#ddd";
  selectedOption = event.target;
});

const dropdownButton = document.getElementById('firstBox');
dropdownButton.addEventListener('click', function(event) {
  event.preventDefault();
});


