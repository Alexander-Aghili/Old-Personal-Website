function enlargeImg(img, modal, modalcontent) {
    modal.style.display = "block";
    modalcontent.src = img.src;
} 

function closeImg(modal) {
    modal.style.display = "none";
}