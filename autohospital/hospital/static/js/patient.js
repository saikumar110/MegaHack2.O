window.onload=initAll;



var saveButton

function initAll() {
    saveButton = document.getElementById('Patient')
    saveButton.onclick= function(){
        var name = document.getElementById('Name').value;
        var Email = document.getElementById('Email').value;
        var Phone = document.getElementById('Phone').value;
        var Password = document.getElementById('Password').value;
        var Age = document.getElementById('Age').value;
        var Primary = document.getElementById('Primary').value;
        var sex = document.getElementById('sex').value;
        var Problems = document.getElementById('Problems').value;
        var Medicine = document.getElementById('Medicine').value;
        
    
        alert(name)
    
        url ='/save_patient?name='+name+"&email="+Email+'&password='+Password+'&sex='+sex+'&Problem='+Problems+'&Age='+Age+'&Primary='+Primary+"&sex="+sex+'&problems='+Problems+"&medicine="+Medicine+"&phone="+Phone;
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

