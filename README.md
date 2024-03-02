# todo-logfy
 An app TO-DO LogFy

---

# Fronend

<img arc="https://github.com/fabioacarvalho/todo-logfy/blob/main/frontend/src/assets/img/logfy_1.png?raw=true">
<br>
<img arc="![image](https://github.com/fabioacarvalho/todo-logfy/assets/84592352/07f84fb2-67da-44bf-bea5-36e61c4c7d69)
">
<br>
<img arc="https://github.com/fabioacarvalho/todo-logfy/blob/main/frontend/src/assets/img/logfy_3.png?raw=true">
<br>
 ---

 # Backend

 ## Starting the project with Docker
 
### Buildind the image Docker

```shell
    docker build -t logfy .
```
<br>

### Starting the container

```shell
    docker run -p 8000:8000 logfy
```

<br>

Acesse: [localhost:8000/admin](localhost:8000/admin)

<br>

---

## Starting locally

### Install the dependencies:

```shell
    pip install -r requirements.txt
```

<br>

### Run migrate:


```shell
    python manage.py migrate
```

<br>

### Create a super user:

```shell
    python manage.py createsuperuser
```
<br>

### Starting the server:

```shell
    python manage.py runserver
```

Acesse: [localhost:8000/admin](localhost:8000/admin)

<br>

---

## Endpoints

<br>

| Endpoint              | Type |
|-----------------------|------|
| board/                | GET  | 
| cards/                | GET  |
| cards/<int:id>/card/  | POST |
| boards/board-create/  | POST |

<br>

## Example

<br>

#### Endpoint: cards/<int:id_board>/card/

| Fields  | Type    | Example       | Required |
|---------|---------|---------------|----------|
| title   | varchar | Create an API | True     |
| content | text    | Create an API | True     |
| user    | int     | 2365          | False    |
| labels  | text    | #CCC          | False    |

<br>

```json

{
    "title": "Create an API",
    "content": "Create an API",
    "status": "draft",
    "labels": "#CCC"
}

```

<br>

#### Endpoint: boards/board-create/

| Fields    | Type    | Example | Required |
|-----------|---------|---------|----------|
| title     | varchar | Draft   | True     |
| creatable | boolean | True    | True     |
| done      | boolean | False   | False    |

<br>

```json

{
    "title": "Done",
    "creatable":false,
    "done":true
}

```

<br>

