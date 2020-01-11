var cartOpen = false;

$('body').on('click', '.js-toggle-cart', toggleCart);

function toggleCart(e) {
  e.preventDefault();
  if(cartOpen) {
    closeCart();
    return;
  }
  openCart();
}

function openCart() {
  cartOpen = true;
  $('body').addClass('open');
}

function closeCart() {
  cartOpen = false;
  $('body').removeClass('open');
}
// Get the modal
var modal = document.getElementById("myModal");

// Get the image and insert it inside the modal - use its "alt" text as a caption
var img = document.getElementsByClassName("riddleImg");

for(let i of img)  {
  i.onclick = function() {
    let modal = document.querySelector(`#M${i.id}`)
    let modalImg = document.querySelector(`#MI${i.id}`)
    var span = document.querySelector(`#MC${i.id}`)
    modal.style.display = "block";
    modalImg.src = this.src;
    span.onclick = function() {
      modal.style.display = "none";
    }
    document.onkeydown = function(evt) {
        modal.style.display = "none";
    }
  }
}
