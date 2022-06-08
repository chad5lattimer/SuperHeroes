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






function fetchData(){
    fetch("https://superheroapi.com/api/access-token/character-id/image")
        .then(response => {
            if(!response.ok){
                throw Error("ERROR");
            }
        return response.json();
        })
        .then(data =>{
            console.log(data.data);
            const html = data.data
                .map(image)
                    return
                    <div class="image">
                        <p><img src= "${image}/p>
                    </div>
        })
}