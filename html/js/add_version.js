
function add_all_list(call) {
    //마인크래프트 버전 리스트를 versions 변수에 저장
    var versions = get_minecraft_versions;
    const myUL = document.getElementById("myUL");

    for (var i = 0; i < myUL.children.length; i++) {
      myUL.children[i].remove();
    }

    for (var i = 0; i < versions.length; i++) {
      const li = document.createElement("li");
      const a = document.createElement("a");
      a.setAttribute("onclick",call + "(\'" + versions[i] + "\')");
      const textNode = document.createTextNode('' + versions[i]);
      a.appendChild(textNode);
      li.appendChild(a);

      myUL.appendChild(li);
    }
}

function add_installed_list(call) {
  var versions = get_installed_versions;
  const myUL = document.getElementById("myUL");

  for (var i = 0; i < myUL.children.length; i++) {
    myUL.children[i].remove();
  }

  for (var i = 0; i < versions.length; i++) {
    const li = document.createElement("li");
    const a = document.createElement("a");
    a.setAttribute("onclick",call + "(\'" + versions[i] + "\')");
    const textNode = document.createTextNode('' + versions[i]);
    a.appendChild(textNode);
    li.appendChild(a);

    myUL.appendChild(li);
  }
}