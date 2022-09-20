var modal = document.getElementById('id001');
var closelist = document.getElementsByClassName('close');
var deletebtn = document.getElementsByClassName('deletebtn');
var cancelbtn = document.getElementsByClassName('cancelbtn');

var targetedlist;

window.onclick = function(event) {
    

    if (event.target == modal) {
        modal.style.display = "none";
    }

    for (var i = 0; i < closelist.length; i++) {
        if (event.target != closelist[i]) {
            continue;
        }
        targetedlist = event.target;
    }

    if (event.target == deletebtn[0]) {
        targetedlist.parentNode.remove();
        modal.style.display = "none";
        targetedlist = null;
    }

    if (event.target == cancelbtn[0]) {
        modal.style.display = "none";
    }
}

//