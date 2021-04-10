window.onload=initAll;

var saveButton


function initAll() {
    saveButton = document.getElementById('submit')
    saveButton.onclick= function(){
        alert()
        var Cp = document.getElementById('Cp').value;
      
        var trestbps = document.getElementById('trestbps').value;
        var chol = document.getElementById('chol').value;
        var fbs = document.getElementById('fbs').value; 
        var thalach = document.getElementById('thalach').value; 
        var exang = document.getElementById('exang').value; 
        var restecg = document.getElementById('restecg').value; 
        
        
    
        url ='/Heart_pre?&trestbps='+trestbps+'&Cp='+Cp+'&chol='+chol+'&fbs='+fbs+'&thalach='+thalach+'&exang='+exang+'&restecg='+restecg;
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

