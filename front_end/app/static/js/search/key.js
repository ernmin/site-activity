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
        // changeDates();
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// function changeDates() {
//     const table = document.querySelector('.dataframe');
//     const targetHeader = "Date";
//     const headers = Array.from(table.rows[0].cells);

//     const colIndex = headers.findIndex(
//         (th) => th.textContent.trim() === targetHeader
//     );

//     if (colIndex !== -1) {
//         for (let i = 1; i < table.rows.length; i++) {
//             const cell = table.rows[i].cells[colIndex];
//             if (cell) {
//                 const dateOnly = cell.textContent.split('T');
//                 cell.textContent = dateOnly[0];
//             }
//         }
//     } else {
//       console.warn(`Header "${targetHeader}" not found.`);
//       document.getElementById('displayResult').innerHTML = 'No Site Activities'

//     }
// }

/*learn error handling here*/




