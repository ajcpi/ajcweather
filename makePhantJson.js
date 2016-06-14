var theData=[];
for (var key in drop["elems"] ) {
    var e = {};
    e['key'] = key;
    e['value'] = drop["elems"][key]['value'];
    theData.push(e)}
return JSON.stringify(theData);


