// Javascript file that adds functionality

let carts = document.querySelectorAll('.add-cart');

let products = [
    {
        name: 'man1',
        tag: 'man1',
        inCart: 0
    },
    {
        name: 'man2',
        tag: 'man2',
        inCart: 0
    },
    {
        name: 'man4',
        tag: 'man4',
        inCart: 0
    },
    {
        name: 'men3',
        tag: 'men3',
        inCart: 0
    },
    {
        name: 'men5',
        tag: 'men5',
        inCart: 0
    },
    {
        name: 'woman4',
        tag: 'woman4',
        inCart: 0
    },
    {
        name: 'women1',
        tag: 'women1',
        inCart: 0
    },
    {
        name: 'women2',
        tag: 'women2',
        inCart: 0
    },
    {
        name: 'women3',
        tag: 'women3',
        inCart: 0
    }
];

for (let i = 0; i < carts.length; i++) {
    carts[i].addEventListener('click', ()=> {
        cartNumbers(products[i]);
    })
} 

function onLoadCartNumbers() {
    let productNumbers = localStorage.getItem('cartNumbers');

    if(productNumbers) {
        document.querySelector('.cart span').textContent = productNumbers;
    }
}

function cartNumbers(product) {
    let productNumbers = localStorage.getItem('cartNumbers');

    productNumbers = parseInt(productNumbers);

    if(productNumbers) {
        localStorage.setItem('cartNumbers', productNumbers + 1);
        document.querySelector('.cart span').textContent = productNumbers + 1;
    } else {
        localStorage.setItem('cartNumbers', 1);
        document.querySelector('.cart span').textContent = 1;
    }

    setItems(product);
    
}

function setItems(product) {
    let cartItems = localStorage.getItem('productsInCart');
    cartItems = JSON.parse(cartItems);

    if (cartItems != null) {
        if (cartItems[product.tag] == undefined) {
            cartItems = {
                ...cartItems,
                [product.tag]: product
            }
        }
        cartItems[product.tag].inCart += 1;
    } else {
        product.inCart = 1;
        cartItems = {
            [product.tag]: product
        }
    }
    localStorage.setItem("productsInCart", JSON.stringify(cartItems));
}
function displayCart() {
    let cartItems = localStorage.getItem("productsInCart");
    cartItems = JSON.parse(cartItems);
    let productContainer = document.querySelector(".products");
    let cartCost = localStorage.getItem('totalCost');

    // console.log(cartItems);
    if (cartItems && productContainer) {
        productContainer.innerHTML = '';
        Object.values(cartItems).map(item => {
            productContainer.innerHTML += `
            <div class="product">
                <ion-icon name="close-circle"></ion-icon>
                <img src="./images/${item.tag}.jpg">
                <span>${item.name}</span>
            </div>
            
            `
        });

        
    }

}
onLoadCartNumbers();
displayCart();