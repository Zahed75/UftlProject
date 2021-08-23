document.querySelector(".minus-btn").setAttribute("disabled", "disabled");
var valueCount
var fueltype = document.getElementById("fuelname").value;
var delivery_charge = document.getElementById("delicharge").innerText;
var octane_price = document.getElementById("opd").innerText;
var diesel_price = document.getElementById("dpd").innerText;
var discont = document.getElementById("discountSelect");
// var price = 65
var discontInput = document.getElementById("discountValue");


function priceTotal() {
    var total = (valueCount * parseInt(diesel_price)) + parseInt(delivery_charge) - parseInt(discontInput.value);
    var base = valueCount * parseInt(diesel_price);
    document.getElementById("price").value = total
    document.getElementById("fuel").value = base

}


discont.addEventListener('change', () => {
    discontInput.value = parseInt(discont.options[discont.selectedIndex].value);

    priceTotal()
});

var discountPrice = discontInput.value


document.querySelector(".plus-btn").addEventListener("click", function() {
    valueCount = document.getElementById("quantity").value;
    valueCount++;
    document.getElementById("quantity").value = valueCount;

    if (valueCount > 20) {
        document.querySelector(".minus-btn").removeAttribute("disabled");
        document.querySelector(".minus-btn").classList.remove("disabled")
    }
    priceTotal()
})
document.querySelector(".minus-btn").addEventListener("click", function() {
    valueCount = document.getElementById("quantity").value;
    valueCount--;
    document.getElementById("quantity").value = valueCount

    if (valueCount == 20) {
        document.querySelector(".minus-btn").setAttribute("disabled", "disabled")
    }
    priceTotal()
})