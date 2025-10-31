const heading = document.getElementById('title');
const items = document.querySelectorAll('.item');

heading.textContent = 'DOM Updated Successfully';

heading.setAttribute('Id', 'head');

const newItem = document.createElement('li');
newItem.textContent = 'New DOM Item Added';
document.querySelector('ul').appendChild(newItem);

// if (items[0]) items[0].remove();


heading.style.color = 'green';
heading.classList.add('highlight');