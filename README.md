# rest
manual to app.py https://habr.com/ru/post/246699/
curl commands :
curl -i http://localhost:5000/todo/api/v1.0/tasks
curl -i http://localhost:5000/todo/api/v1.0/tasks/2
curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' http://localhost:5000/todo/api/v1.0/tasks
manual to dockerfile https://habr.com/ru/post/310460/
dockerhub vasiariabov/rest3 - it run, but not work :(
