const caller = document.getElementById("bs_offer"); // get a reference to the button node

// This function will be called when the HTML page loaded
function ready()
{
    // Setup event listener for mouseenter
    caller.addEventListener("mouseenter", function (ev)
    {
        const randX = Math.floor(Math.random() * (window.innerWidth - 100));
        const randY = Math.floor(Math.random() * (window.innerHeight - 100));
        console.log([randX, randY]);
        caller.style.left = randX + 'px';
        caller.style.top = randY + 'px';
    });

    // Set a click listener just in case the user manages to hit the button
    caller.addEventListener("click", function (ev)
    {
        alert(`
           Wow! You Managed to Click it! 
        (but still no gift card for you...)`)
    })
}
