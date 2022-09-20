function myFunction(enter) {

    let first = document.getElementById("skin");
    let second = document.getElementById("jvm");
    let third = document.getElementById("other");
    
    switch(enter) {
        case 1:
            switching(first);
            second.style.display = "none";
            third.style.display = "none";
            break;
        case 2:
            switching(second);
            first.style.display = "none";
            third.style.display = "none";
            break;
        case 3:
            switching(third);
            second.style.display = "none";
            first.style.display = "none";
            break;
    }
    
}



function switching(doc) {
    if (doc.style.display === "none") {
        doc.style.display = "block";
    }
} 