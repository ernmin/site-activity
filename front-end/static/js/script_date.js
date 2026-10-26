document.querySelector('#siteForm').addEventListener('submit', (event) => {
    event.preventDefault();
    get_dates();
    // submitID();
})

async function get_dates() {
    await submitID();
    // hyper_link();
}


function submitID() {
    const userID = document.querySelector('#getID').value;
    // document.getElementById('displayResult').innerText = userID;
    return fetch('/rows', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ requestedUser: userID })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('displayResult').innerHTML = data.result;
        if (data.result == 'You have clicked too many times, try again in a minute'){
            const disableButton = document.querySelector('button');
            disableButton.disabled = true;
            setTimeout(() => {
            disableButton.disabled = false;
            }, 5000);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}




