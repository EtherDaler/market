window.onload = async function () {
  let res = await getProducts();
  for (let i in res.data) {
    console.log(i)
    let li = document.createElement("li");
    let n = res.data[i].name;
    let d = res.data[i].description;
    let p = res.data[i].price;
    let x = document.createElement('span');
    let y = document.createElement('span');
    let z = document.createElement('span');
    x.innerText = n;
    y.innerText = d;
    z.innerText = p;
    li.appendChild(x);
    li.appendChild(document.createElement('br'));
    li.appendChild(y);
    li.appendChild(document.createElement('br'));
    li.appendChild(z);
    document.getElementById("myUL").appendChild(li);
  }

}

async function newElement() {
  let li = document.createElement("li");
  let inputName = document.getElementById("nameInput").value;
  let inputDiscr = document.getElementById("discrInput").value;
  let inputPrice = document.getElementById("priceInput").value;
  let name = document.createTextNode(inputName);
  let discr = document.createTextNode(inputDiscr);
  let price = document.createTextNode(inputPrice);
  li.appendChild(name);
  li.appendChild(document.createElement('br'));
  li.appendChild(discr);
  li.appendChild(document.createElement('br'));
  li.appendChild(price);
  if (inputName === '' || inputDiscr === '' || inputPrice === '') {
    alert("You must write something!");
  } else {
    document.getElementById("myUL").appendChild(li);
  }
  let res = await createProducts(inputName, inputDiscr, inputPrice);
  document.getElementById("nameInput").value = "";
  document.getElementById("discrInput").value = "";
  document.getElementById("priceInput").value = "";
}

async function getProducts() {
  const res = await fetch("/api/v1/products/", {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });
  try {
    return {
      res,
      data: await res.json(),
    };
  } catch {
    return {
      res,
      detail: "внутренняя ошибка сервера",
    };
  }
}

async function createProducts(name, descr, price) {
  const res = await fetch("/api/v1/products/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ name:  name, description: descr, price: price, date_of_create: '2012-04-23T18:25:43.511Z'})
  });
  try {
    return {
      res,
      data: await res.json(),
    };
  } catch {
    return {
      res,
      detail: "внутренняя ошибка сервера",
    };
  }
}