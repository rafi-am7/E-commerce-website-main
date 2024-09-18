
var updateBtns = document.getElementsByClassName('update-cart');
for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product;
        var action = this.dataset.action;
        console.log('productId:', productId, 'action:', action);
        console.log('User:', user);

        if (user === 'AnonymousUser') {
            console.log('User is not logged in');
        } else {
            console.log('User is logged in');
            updateUserOrder(productId, action); 
        }
    });
}

function updateUserOrder(productId, action) {
    var url = '/update_item/';
    fetch(url, {
        method: 'POST', 
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({ 'productId': productId, 'action': action })
    }).then(function (response) {
        if (!response.ok) {
            throw new Error('Failed to update item');
        }
        return response.json();
    }).then(function (data) {
        location.reload();
        console.log(data);
    }).then(function (error) {
        console.error('Error:', error);
    });
}
