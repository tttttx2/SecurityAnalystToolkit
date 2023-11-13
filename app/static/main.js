$.getJSON('plugins', function(data) {
  console.log(data);
  data.forEach((element) => {
    document.getElementById("navbar").innerHTML +='<li class="nav-item">\n<a href="#'+element+'" id="nav_item_'+element+'" class="nav-link text-white" aria-current="page" onclick="load_content(\''+element+'\')"><svg class="bi pe-none me-2" width="16" height="16"><use xlink:href="#home"/></svg>'+element+'</a></li>'
  });
});


function load_content(plugin) {
  $.getJSON('plugins/'+plugin, function(data) {
    console.log(data);
    document.getElementById("content").innerHTML = ''
    data.forEach((element) => {
      document.getElementById("content").innerHTML += '<button onclick="start_feature(\''+plugin+'\', \''+element+'\')" class="btn btn-primary p-2" id="feature_button_'+element+'" type="button">'+element+'</button><br>'
    });
    document.getElementById("content").innerHTML += ''
  });
}

function start_feature(plugin, feature) {
  arg1 = document.getElementById('arg1').value
  if (arg1 == ''){
    alert("Please enter something in the input field on top.")
  }
  document.getElementById("feature_button_"+feature).disabled = true;
  $.getJSON('plugins/'+plugin+'/'+feature+'?data='+arg1, function(data) {
    console.log(data);
    document.getElementById("results").innerHTML = '<code>>'+plugin+'/'+feature+' '+arg1+'\n'+data['pretty']+'</code>\n\n'+document.getElementById("results").innerHTML
    // document.getElementById("results").scrollTop = document.getElementById("results").scrollHeight;
    hljs.highlightAll();
    document.getElementById("feature_button_"+feature).disabled = false

  }).fail(function() { alert("Error with module "+plugin+"/"+feature); });
}
