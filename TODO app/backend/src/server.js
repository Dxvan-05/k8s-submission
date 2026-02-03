const express = require('express')
const { Client } = require('pg')

const PORT = process.env.PORT || 9999

const client = new Client({
  host: process.env.POSTGRES_HOST || 'postgres-svc',
  port: process.env.POSTGRES_PORT || 5432,
  database: process.env.POSTGRES_DB || 'tododb',
  user: process.env.POSTGRES_USER || 'todouser',
  password: process.env.POSTGRES_PASSWORD || 'password'
})

const app = express()

app.use(express.text())

client.connect()

app.get('/todos', async (req, res) => {
  try {
    const result = await client.query('SELECT * FROM todos')
    res.send(result.rows.map(row => row.todo))
  } catch (err) {
    console.error(err)
    res.status(500).send('Error retrieving todos')
  }
})

app.post('/todos', async (req, res) => {
  const newTodo = req.body
  if (!newTodo || newTodo.length > 140) {
    return res.status(400).send('Todo must be non-empty and less than 140 characters')
  }
  try {
    const result = await client.query('INSERT INTO todos (todo) VALUES ($1) RETURNING *', [newTodo])
    res.status(201).send(result.rows[0])
  } catch (err) {
    console.error(err)
    res.status(500).send('Error creating todo')
  }
})

app.listen(PORT, () => {
    console.log('Todo backend server is running on port ' + PORT) 
})

