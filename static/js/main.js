window.addEventListener('load', function() {
    const tg = window.Telegram.WebApp;
    tg.expand(); // Expand the web app to full height

    const userData = tg.initDataUnsafe;

    // Send user data to the backend
    fetch('/api/user-data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') // Django's CSRF token
        },
        body: JSON.stringify({
            telegram_data: userData
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });

    const playButton = document.querySelector('.play-button');
    const betAmountInput = document.querySelector('.bet-amount');
    const boxes = document.querySelectorAll('.box');

    playButton.addEventListener('click', () => {
        const betAmount = betAmountInput.value;
        if (betAmount) {
            // TODO: Implement game start logic
            console.log(`Playing with bet: ${betAmount}`);
            resetGrid();
        } else {
            alert('Please enter a bet amount.');
        }
    });

    boxes.forEach(box => {
        box.addEventListener('click', () => {
            // TODO: Implement box click logic
            console.log('Box clicked');
            box.classList.add('clicked');
        });
    });

    function resetGrid() {
        boxes.forEach(box => {
            box.classList.remove('clicked', 'bomb');
        });
    }

});

// Function to get CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}