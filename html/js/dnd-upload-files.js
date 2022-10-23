const dropZone = document.querySelector('.drag-area');

let file; //this is a global variable and we'll use it inside multiple functions

dropZone.addEventListener('dragover', (e) => {
    e.preventDefault();
});

dropZone.addEventListener('drop', (e) => {
    e.preventDefault();
    for(let file of e.dataTransfer.files) {
        py_print(file.path);
    }
}); 