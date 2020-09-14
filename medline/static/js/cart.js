updateBtns = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        productId = this.dataset.product
        action = this.dataset.action
        console.log('productId: ', productId, 'Action:', action)


        console.log('USER:', user)
        if (user !== 'AnonymousUser'){
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId, action){
    console.log('User is logged in, sending data..')

    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action':action})
    })

    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        console.log('data:', data)
        location.reload()
    })
    
}