window.onload=initAll;



var saveButton

function initAll() {
    saveButton = document.getElementById('save')
    saveButton.onclick= function(){
        var name = document.getElementById('examplename').value;
        var email = document.getElementById('exampleInputEmail1').value;
        var password = document.getElementById('exampleInputPassword1').value;
    
        /* alert(name)
        alert(email)
        alert(password) */
    
        url ='/Create_acc?name='+name+"&email="+email+'&password='+password;
        var req = new XMLHttpRequest();
        req.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                alert(req.responseText);
               
            }
        };
        req.open("GET", url, true);
        req.send();
    }
}


/* =------------------Signup Form --------------------- */

