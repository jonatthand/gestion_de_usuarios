const API_URL = "https://gestion-de-usuarios-pums.onrender.com"

async function getNotifications() {
    const response = await fetch(`${API_URL}/notifications`);
    const data = await response.json();

    console.log(data);
}

function showMessage(msg, type="success"){
    const el = document.getElementById("message");

    el.innerText = msg;

    if(type === "error"){
        el.style.color = "red";
    } else {
        el.style.color = "green";
    }
}

function showTempMessage(elementId, msg, type="success"){

    const el = document.getElementById(elementId);

    el.innerText = msg;
    el.style.color = type === "error" ? "red" : "green";

    setTimeout(()=>{
        el.innerText = "";
    }, 3000);
}

// ---------------- AUTH ----------------

async function register(){
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const res = await fetch(API + "/auth/register",{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({email,password})
    });

    const data = await res.json();

    if(!res.ok){
        showMessage("Error: " + data.detail);
        return;
    }

    showMessage("Cuenta creada correctamente");
}

async function login(){
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const res = await fetch(API + "/auth/login",{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({email,password})
    });

    const data = await res.json();

    if(!res.ok){
        showMessage("Error: " + data.detail);
        return;
    }

    localStorage.setItem("token", data.access_token);

    showMessage("Login exitoso");

    setTimeout(()=>{
        window.location.href = "dashboard.html";
    },1000);
}

// ---------------- TOKEN ----------------

function getToken(){
    return localStorage.getItem("token");
}

function logout(){
    localStorage.removeItem("token");
    window.location.href = "index.html";
}

// ---------------- CREATE ----------------

async function createNotification(){

    const res = await fetch(API + "/notifications",{
        method:"POST",
        headers:{
            "Content-Type":"application/json",
            "Authorization":"Bearer " + getToken()
        },
        body:JSON.stringify({
            title: document.getElementById("title").value,
            message: document.getElementById("messageInput").value,
            channel: document.getElementById("channel").value,
            recipient: document.getElementById("recipient").value
        })
    });

    const data = await res.json();

    if(!res.ok){
        showTempMessage("msg-create", "❌ " + data.detail, "error");
        return;
    }

    showTempMessage("msg-create", "✔ Notificación creada");
}

// ---------------- GET ALL ----------------

async function getNotifications(){

    const res = await fetch(API + "/notifications",{
        headers:{
            "Authorization":"Bearer " + getToken()
        }
    });

    const data = await res.json();

    if(!res.ok){
        showTempMessage("msg-list", "❌ " + data.detail, "error");
        return;
    }

    const list = document.getElementById("list");
    list.innerHTML = "";

    data.forEach(n=>{
        list.innerHTML += `<li>${n.id} - ${n.title} - ${n.status}</li>`;
    });

    showTempMessage("msg-list", "✔ Notificaciones cargadas");
}

// ---------------- GET BY ID ----------------

async function getById(){

    const id = document.getElementById("getId").value;

    const res = await fetch(API + "/notifications/" + id,{
        headers:{
            "Authorization":"Bearer " + getToken()
        }
    });

    const data = await res.json();

    if(!res.ok){
        showTempMessage("msg-get", "❌ " + data.detail, "error");
        return;
    }

    document.getElementById("getResult").innerText = JSON.stringify(data,null,2);

    showTempMessage("msg-get", "✔ Encontrada");
}

// ---------------- UPDATE ----------------

async function updateNotification(){

    const id = document.getElementById("updateId").value;

    const res = await fetch(API + "/notifications/" + id,{
        method:"PATCH",
        headers:{
            "Content-Type":"application/json",
            "Authorization":"Bearer " + getToken()
        },
        body:JSON.stringify({
            title: document.getElementById("newTitle").value
        })
    });

    const data = await res.json();

    if(!res.ok){
        showTempMessage("msg-update", "❌ " + data.detail, "error");
        return;
    }

    showTempMessage("msg-update", "✔ Actualizada");
}

// ---------------- DELETE ----------------

async function deleteNotification(){

    const id = document.getElementById("deleteId").value;

    const res = await fetch(API + "/notifications/" + id,{
        method:"DELETE",
        headers:{
            "Authorization":"Bearer " + getToken()
        }
    });

    if(!res.ok){
        const data = await res.json();
        showTempMessage("msg-delete", "❌ " + data.detail, "error");
        return;
    }

    showTempMessage("msg-delete", "✔ Eliminada");
}