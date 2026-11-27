document.querySelector('#keyForm').addEventListener('submit', (event) => {
    event.preventDefault();
    get_activity();
    // submitID();
})

async function get_activity() {
    await submitID();
    // hyper_link();
}


function submitID() {
    const siteID = document.querySelector('#siteID').value;
    // document.getElementById('displayResult').innerText = dateFrom + ' ' + dateTo;
    return fetch('/searchkey', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            siteID: siteID
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
        document.getElementById('displayResult').innerHTML = data.result;
        changeDates();
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function changeDates() {
    const table = document.querySelector('.dataframe');
    const targetHeader = "Date";
    const dateRow = table && Array.from(table.rows).find(
        (row) => row.cells[0] && row.cells[0].textContent.trim() === targetHeader
    );

    if (dateRow) {
        for (let i = 1; i < dateRow.cells.length; i++) {
            const cell = dateRow.cells[i];
            cell.textContent = cell.textContent.trim().split('T')[0];
        }
    } else {
        console.warn(`Row "${targetHeader}" not found.`);
        document.getElementById('displayResult').innerHTML = 'No Site Activities';
    }
}

/*learn error handling here*/




