/*
 * Toggle whether the small navbar is opened or closed.
 */
function openHamburger() {
    var x = document.getElementById("navbar");
    if (x.className === "closed") {
        x.className = "open";
    } else {
        x.className = "closed";
    }
}

/* Make all previews clickable. */
function viewPreviewCard() {
    window.location = this.getAttribute('href');
}

let previews = document.getElementsByClassName('card preview');
for (let i=0; i<previews.length; i++) {
    let card = previews[i];
    console.log(card);
    previews[i].onclick = viewPreviewCard;
}