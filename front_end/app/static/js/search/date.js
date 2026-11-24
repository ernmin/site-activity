document.querySelector('#dateForm').addEventListener('submit', (event) => {
    event.preventDefault();
    get_dates();
    // submitID();
})

async function get_dates() {
    await submitDates();
    // hyper_link();
}


function submitDates() {
    const dateFrom = document.querySelector('#dateFrom').value;
    const dateTo = document.querySelector('#dateTo').value;
    // document.getElementById('displayResult').innerText = dateFrom + ' ' + dateTo;
    return fetch('/searchdate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
            searchFrom: dateFrom,
            searchTo: dateTo 
        })
    })
    .then(response => response.json())
    .then(data => {
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
    const headers = Array.from(table.rows[0].cells);

    const colIndex = headers.findIndex(
        (th) => th.textContent.trim() === targetHeader
    );

    if (colIndex !== -1) {
        for (let i = 1; i < table.rows.length; i++) {
            const cell = table.rows[i].cells[colIndex];
            if (cell) {
                const dateOnly = cell.textContent.split('T');
                cell.textContent = dateOnly[0];
            }
        }
    } else {
      console.warn(`Header "${targetHeader}" not found.`);
    }
}

/*learn error handling here*/




