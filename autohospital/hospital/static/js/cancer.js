window.onload=initAll;

var saveButton


function initAll() {
    saveButton = document.getElementById('submit')
    saveButton.onclick= function(){
        var Concave = document.getElementById('Concave').value;
      
        var Area = document.getElementById('Area').value;
        var Radius = document.getElementById('Radius').value;
        var Perimeter = document.getElementById('Perimeter').value; 
        var Concavity = document.getElementById('Concavity').value; 
        var body = document.getElementsByClassName('modal-body')
        
    
        url ='/cancer_pre?&Perimeter='+Perimeter+'&Concavity='+Concavity+'&Radius='+Radius+'&Area='+Area;
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

