document.querySelector('#userIDForm').addEventListener('submit', (event) => {
    event.preventDefault();
    ID_hyper_link();
    // submitID();
})

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

function hyper_link() {
    const rows = document.querySelectorAll('table tbody tr')

    rows.forEach(row => {
    // Select the second cell (index 1, as JavaScript is 0-indexed)
    const secondCell = row.cells[1];
    secondCell.classList.add('second-cell')
    
    if (secondCell) {
        // Get the plain text URL from the cell
        const url = secondCell.textContent.trim();
        
        new_url = change_link(url);
        
        // Ensure the cell is not empty before creating the link
        // if (new_url == 'You clicked too much'){
        //     return
        // }
        // else 
        if (new_url != url) {
            // Rewrite innerHTML as a hyperlink
            secondCell.innerHTML = `<img src="${new_url}">`;
        }
        else {
            secondCell.innerHTML  = `<a href="${url}" target="_blank">${url}</a>`;
        }
    }
    const links = document.querySelectorAll('a');

    links.forEach((a_tag, index) => {
    a_tag.textContent = `Photo ${index + 1}`;
});
});
}

function change_link(url) {
    const match = url.match(/(?:\/d\/|id=)([\w-]+)/);
    if (match && match[1]) {
        const fileID = match[1];
        // return `https://drive.google.com/thumbnail?id=${fileID}&sz=w250`
        return `https://lh3.googleusercontent.com/d/${fileID}`
    }
    return url
}

async function ID_hyper_link() {
    await submitID();
    hyper_link();
}


