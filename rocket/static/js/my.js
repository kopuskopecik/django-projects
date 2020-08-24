
const text = document.querySelector(".abc");
text.style.display = "block";

const buttons = document.querySelectorAll(".isim");

const contents = document.querySelectorAll(".abc");

for (const button of buttons) {
    console.log(button);
    
    button.addEventListener('click', function(event) {
        for (const elm of contents) {
            elm.style.display = "none";
        };

    let content = document.getElementById(event.target.id + "-1");
    content.style.display = "block";
    })
};
