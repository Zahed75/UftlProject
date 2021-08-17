document.querySelector(".minus-btn").setAttribute("disabled", "disabled");
var valueCount
var price = 65

function priceTotal() {
    var total = valueCount * price + 105;
    var base = valueCount * price;
    document.getElementById("price").innerText = total + '/-'
    document.getElementById("fuel").innerText = base + '/-'
}
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