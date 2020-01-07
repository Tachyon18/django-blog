var title = document.querySelector('input[name=title]');
var slugInput = document.querySelector('input[name=slug]');


const slugify = (val)=>{
  return val.toString().toLowerCase().trim().replace(/&/g, '-and-').replace(/[\s\W-]+/g, '-')
};

title.addEventListener('keyup', (e)=>{
  slugInput.setAttribute('value', slugify(title.value))
})
