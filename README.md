# nucleus-cloud-challenge

A small HTTPS web service built with Python and Flask, running in Docker. Built as part of a cloud engineering challenge

## What it does

- Serves a webpage over HTTPS at `https://localhost:8443`
- Has a `/health` endpoint that returns `{"status": "ok"}`
- Logs every request to the console
- Uses a self-signed SSL cert for local HTTPS


## How to run it

You just need Docker installed

**1. Clone the repo**
git clone https://github.com/TemiOwojuyigbe/nucleus-cloud-challenge.git
cd nucleus-cloud-challenge



**2. Start the service**
docker compose up --build



**3. Open your browser and go to**
https://localhost:8443



You'll get a security warning because of the cert, click Advanced and proceed, and its expected.

Health check:
https://localhost:8443/health




## How the SSL cert was generated

openssl req -x509 -newkey rsa:2048 -keyout certs/key.pem -out certs/cert.pem -days 365 -nodes -subj "/CN=localhost"



The cert and key live in the `certs/` folder and get mounted into the container as read-only

## Why I made the choices I did

I picked Flask because it's simple and you dont need to use something complex for a service this samll. Im really juist definign routes in a few lines and im very comforatble with python and its very easy to read

Port 8443 instead of 443 because 443 requires admin permissions to bind to so 8443 is the common workaround for local HTTPS

I made the certs mount to the docker volume instead being copied into the image so the image itself doesnt contain the key

## What I'd improve with more time

- Replace Flask's dev server with Gunicorn beacuse Flask itself warns you at startup that it's not production ready
- I would add timestamps to the logs so you can tell when each request actually came in
- I would add proper error handling for 404s and 500s instead of only relying on Flask defaults


## How I'd deploy this to GCP

I'd push the Docker image to Artifact Registry, then run it on Cloud Run. you hand it an image and it handles running it, scaling, and HTTPS automatically with a real trusted cert. No servers to manage


## Why storing a private SSL key in a repo is bad

The private key is basically the password to your server. If it ends up in a public repo anyone who clones it has a copy and even if you delete it, git history keeps it forever

With your key someone could impersonate your server or decrypt captured traffic. The right move is to store secrets in something like GCP Secret Manager and inject them at runtime so they never touch the codebase


## AI tools used

I used Claude to help me work through parts of this such as understanding Docker volumes, and talking through the GCP deployment. The code and decisions are mine, Claude just helped me get unstuck when I needed it