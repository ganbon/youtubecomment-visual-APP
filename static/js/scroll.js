function down(){
var element = document.documentElement;
var bottom = element.scrollHeight - element.clientHeight;
window.scroll({
    top: bottom,
    behavior: "smooth"
});
}
