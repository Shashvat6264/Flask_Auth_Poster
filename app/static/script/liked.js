function like(id){
    var xhr = new XMLHttpRequest();
    var url = "http://127.0.0.1:5000/liked";    
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    var data = JSON.stringify({"id": id});
    xhr.send(data);
};