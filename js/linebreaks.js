function insertLineBreaks(selector, wordsPerLine) {
    const element = document.querySelector(selector);
    const text = element.innerText;
    const words = text.split(' ');
    let newText = '';

    for (let i = 0; i < words.length; i += wordsPerLine) {
        newText += words.slice(i, i + wordsPerLine).join(' ') + '<br>';
    }

    element.innerHTML = newText;
}

document.addEventListener('DOMContentLoaded', function() {
    insertLineBreaks('#content', 100);
});