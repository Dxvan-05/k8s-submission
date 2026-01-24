const express = require('express')


const PORT = process.env.PORT || 9999

todos = []

const app = express()

app.use(express.text())

app.get('/todos', (req, res) => {
    res.send(todos)
})

app.post('/todos', (req, res) => {
    const newTodo = req.body
    todos.push(newTodo)
    res.status(201).send(newTodo)
})

app.listen(PORT, () => {
    console.log('Todo backend server is running on port ' + PORT) 
})

