# Issues
I faced the problem that flask server isn't running in HTTPS.
I found onine that I must integrate an openssl cerificate and key.
# Solution
use ubuntu wsl to generate ths openssle with
`openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365`

# issue
Running in production requires gunicorn that relieso n fcntl that is not available on windows
# Solution
use docker

