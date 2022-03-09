function AddCondition() {
    var mi=-1;
    const sc = [...document.querySelectorAll('#search_conditions > div')];
    // find the max data-index used so far
    for(var i=0;i<sc.length;i++){
        nv = parseInt(sc[i].getAttribute('data-index'))
        if (nv > mi) mi = nv;
    }
    // retrieve the template and make a copy of it
    var template = document.getElementById("conditions-_-form");
    mi +=1
    tc = template.cloneNode(true);
    tc.hidden =false
    tc.setAttribute('id','conditions-'+mi+'-form')
    // update the ids and the names of every field with a unique data-index 
    tc.setAttribute('data-index',mi)
    const selects = tc.getElementsByTagName('select')
    mi +=1
    for(var i=0;i<selects.length;i++){
        selects[i].setAttribute('id',selects[i].id.replace("-_-","-"+mi+"-"))
        selects[i].setAttribute('name',selects[i].name.replace("-_-","-"+mi+"-"))
    }
    const inputs = tc.getElementsByTagName('input')
    for(var i=0;i<inputs.length;i++){
        inputs[i].setAttribute('id',inputs[i].id.replace("-_-","-"+mi+"-"))
        inputs[i].setAttribute('name',inputs[i].name.replace("-_-","-"+mi+"-"))
    }
    // append the new object to the search_condition
    document.getElementById('search_conditions').appendChild(tc);
}

