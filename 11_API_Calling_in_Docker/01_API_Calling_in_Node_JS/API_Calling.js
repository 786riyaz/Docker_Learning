fetch('https://dummyjson.com/products')
  .then(res => res.json())
  .then(json => console.log(json));