let now = new Date();
let menuSections = document.querySelectorAll(".menu-section-item")
let menuContents = document.querySelectorAll(".menu-section-content")
let datetimeLocal = now.toISOString().slice(0,16);
// let menuContent = document.querySelectorAll()
document.getElementById("datetime").value = datetimeLocal

function handleLinkClick(event) {
    event.preventDefault();
    // event.stopPropagation();
}

function showFood(event) {
    const divFood = document.getElementById('food-select')
    const category = event.target.value

    divFood.innerHTML = ""
    console.log(event.target.value)

    foods = {
        "Pizza": ["Margherita", "Formaggio","Chicken", "Pineapple'o'clock", "Meat Town", "Parma"],
        "Salads": ["Lasagna", "Ravioli", "Spaghetti Classics", "Seafood pasta"],
        "Starter": ["Today's Soup", "Bruschetta", "Garlic bread", "Tomozzarella"]
    }

    var getList = foods[category]
    console.log(getList)
    console.log(divFood)
    getList.forEach(function(food) {
        const option = document.createElement('option')
        console.log(food)

        option.value = food
        option.text = food
        divFood.appendChild(option)
    })
    
}

function openMenu(event, section) {
 
    for (let i = 0; i < menuSections.length; i++) {
        const item = menuSections[i]
        item.classList.remove('web-red')
    }
    
    const divElement = event.target.closest('.menu-section-item')
    divElement.classList.add('web-red')
    
    for (let i = 0; i < menuContents.length; i++) {
        const content = menuContents[i]
        content.style.display = 'none'
    }

    const showMenu = document.getElementById(section)
    showMenu.style.display = 'block'
    
}

