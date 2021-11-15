# pdf writer service

Service for casting html files and save them as pdf.

We uses at python in version 3.7, and Flask in version 1.1.4.

## Usage example

```js
import fetch from 'node-fetch'
import { writeFile } from 'fs';

let fileName = 'exapmleFile';

# make fetch post request to pdf service with html as body
# then save the response as pdf file
fetch('http://localhost:3001/writer', { 
    method: "POST", 
    body: JSON.stringify({'file': '<div style="color:#006699;">Elazar Deri the king!</div>', fileName })
    })
.then(res => res.buffer())
.then(buf => writeFile(`./${fileName}.pdf`, buf, () => {}))
```

## What necessary to run the service on docker container?

From [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html) we downloaded the distribution **Amazon Linux** in architectures **x86_64**.
(for running locally on windows, download the proper version)

We made an Dockerfile with the commands below,
and requirements.txt for the packages.

Then we create the docker container.

### Comments

Build the docker
```bash
docker build -t pdf-service .
```

Run the docker (locally)
```bash
docker run -it -p 3001:3001 pdf-service
```

Build an tgz file
```bash
docker save pdf-service -o pdf-service.tgz
```

### Eventually
Publish the tgz image in your favorite registry (like artifactory)
And then run the image in your favorite container menegment (like openshift)