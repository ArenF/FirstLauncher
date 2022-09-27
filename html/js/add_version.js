

function call_minecraft_versions(versions, func) {
  const myUL = document.getElementById("myUL");
  createLists(myUL, versions, func);
}

function call_installed_versions(versions, func) {
  const myUL = document.getElementById("myUL");
  createLists(myUL, versions, func);
}

function createLists(myUL, versions, func) {
  for (var i = 0; i < myUL.children.length; i++) {
    myUL.children[i].remove();
  }

  for (var i = 0; i < versions.length; i++) {
    const li = document.createElement("li");
    const a = document.createElement("a");
    a.setAttribute("onclick", func + "(\'" + versions[i] + "\')");
    const textNode = document.createTextNode('' + versions[i]);
    a.appendChild(textNode);
    li.appendChild(a);

    myUL.appendChild(li);
  }
}

