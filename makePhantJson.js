var theData=[];
for (var key in drop["elems"] ) {
    var e = {***REMOVED***;
    e['key'] = key;
    e['value'] = drop["elems"][key]['value'];
    theData.push(e)***REMOVED***
return JSON.stringify(theData);


