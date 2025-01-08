var updtaeBtns = document.getElementsByClassName('update-cart');

for (var i = 0; i < updtaeBtns.length; ++i) {
    updtaeBtns[i].addEventListener('click', function() {
        var productId = this.dataset.product;
        var action = this.dataset.action;

        console.log('productId - ', productId, 'action: ', action)

        if (user == 'AnonymousUser') {
            addCokkieItem(productId, action)
        } else {
            updateUserorder(productId, action);
        }
    })

}

function addCokkieItem(productId, action) {
    if (action == 'add') {
        if (cart[productId] == undefined) {
            cart[productId] = { 'quantity': 1 }
        } else {
            cart[productId]['quantity'] += 1
        }
    }
    if (action == 'remove') {
        cart[productId]['quantity'] -= 1

        if (cart[productId]['quantity'] <= 0) {
            console.log('remove item...')
            delete cart[productId]
        }
    }
    console.log('Cart:', cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    location.reload()

}

function updateUserorder(productId, action) {
    console.log('sending..........')

    var url = '/updateItem/'

    fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({
                'productId': productId,
                'action': action
            })
        })
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            console.log('data:', data)
            location.reload()
        })


}