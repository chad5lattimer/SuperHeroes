fetch('https://superheroapi.com/api/access-token/character-id/biography')
    method: 'GET'
    .then(res => {
        if (res.ok) {
        console.log('SUCCESS')   
        } else {
        console.log('Not Successful')
        }
})
.then(data => console.log(data))
.catch(error => console.log('Error'))




