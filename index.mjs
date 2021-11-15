import fetch from 'node-fetch'
import {writeFile} from 'fs';

let fileName = 'מסדרים-2021';
fetch('http://localhost:3001/writer', {method: "POST", body:JSON.stringify({'file': '<div style="color:#006699;">Elazar the king!</div>', fileName})})
.then(res => res.buffer())
.then(buf => writeFile(`./${fileName}.pdf`, buf, () => {}))