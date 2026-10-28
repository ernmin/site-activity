document.querySelector('#siteForm').addEventListener('submit', (event) => {
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
    document.getElementById('displayResult').innerText = dateFrom;
    // return fetch('/appdates', {
    //     method: 'POST',
    //     headers: { 'Content-Type': 'application/json' },
    //     body: JSON.stringify({ 
    //         searchfrom: dateFrom,
    //         searchto: dateTo 
    //     })
    // })
    // .then(response => response.json())
    // .then(data => {
    //     document.getElementById('displayResult').innerHTML = data.result;
    // })
    // .catch(error => {
    //     console.error('Error:', error);
    // });
}


/*learn error handling here*/




