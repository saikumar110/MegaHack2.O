window.onload=initAll;

var saveButton


function initAll() {
    saveButton = document.getElementById('save')
    saveButton.onclick= function(){
        var name = document.getElementById('name').value;
        var age = document.getElementById('age').value;

        var number = document.getElementById('number').value;
        var query = document.getElementById('query').value;
        var date = document.getElementById('date').value;
    
       /*  alert(name)
        alert(age)
        alert(number)
        alert(query)
        alert(date) */
        
    
        url ='/appoint?name='+name+"&age="+age+'&number='+number+'&query='+query+'&date='+date;
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

