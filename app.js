//http://172.16.10.20:1000/login?
//application/x-www-form-urlencoded

//http://www.gstatic.com/generate_204
//const superagent = require('superagent').agent()
const fetch = require('node-fetch');
const ytm = () => {
    
    fetch('http://www.gstatic.com/generate_204').then(res => res.text()).then(body => {
    
    body=body.split('?')[1]
    body=body.split('"')[0]
    console.log(body);
    fetch('http://172.16.10.20:1000/fgtauth?'+body)
//     payload={
//         '4Tredir': 'http%3A%2F%2Fwww.gstatic.com%2Fgenerate_204',
//         'magic': body,
//         'username': 'pavangupta_cs20',
//         'password': 'GLA#t45sd8',
// }
// payload = {
//     '4Tredir': 'http%3A%2F%2Fwww.gstatic.com%2Fgenerate_204',
//     'magic': body,
//     'username': 'pavangupta_cs20',
//     'password': 'GLA#t45sd8',
//     }
        var fd=new FormData();
        fd.append(  '4Tredir','http%3A%2F%2Fwww.gstatic.com%2Fgenerate_204');
        fd.append(  'magic', body);
        fd.append( 'username', 'pavangupta_cs20');
        fd.append(  'password', 'GLA#t45sd8');
    console.log(fd)
    fetch('http://172.16.10.20:1000/fgtauth?'+body, {method: 'POST', body: fd })
    .then(res => res.text())
    .then(json => console.log(json));

    });
    
    //body=body.split('?')[1]
    //body=body.split('"')[0]
   

    //let dashboard = await superagent
    //.post('http://172.16.10.20:1000/')
    //.send({ username: 'pavangupta_cs20', password: 'GLA#t45sd8'})
    //.set('Content-Type', 'application/x-www-form-urlencoded');
    // console.log(dashboard.text);
};

ytm();