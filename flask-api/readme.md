# Building an API with Flask
## Route creation, Error Handling and HTTP Requests

This code snippet creates three routes:
- <code>/</code>
- <code>/no_content</code>
- <code>/exp</code>

1. First, tou need to start a flask server. Run the following command in the root directory 
```
flask --app server --debug run
```
2.  In another terminal, use the following CURL commands with <code>localhost:5000/</code>
<code>localhost:5000/no_content</code>
<code>localhost:5000/exp</code>
```
curl -X GET -i -w '\n' localhost:5000
```
```
curl -X GET -i -w '\n' localhost:5000/no_content
```
```
curl -X GET -i -w '\n' localhost:5000/exp
```