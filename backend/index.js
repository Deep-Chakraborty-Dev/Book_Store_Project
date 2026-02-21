import express from 'express'
import mongoose from 'mongoose';
const app = express()
import dotenv from 'dotenv'
dotenv.config();

import cors from 'cors'
import router from './src/books/Bookroute.js'

const bookroutes = router;


const port = process.env.PORT || 5000

app.use(express.json());
app.use(cors({
  origin:['http://localhost:5173'],
  credentials:true
}))

app.use('/api/books',bookroutes)

async function main() {
  await mongoose.connect(process.env.DB_URL);
    app.use('/', (req, res) => {
    res.send('Book server is listening')
  })
}

main().then(() => console.log("mongodb connected successfully!")).catch(err => console.log(err));

app.listen(port, () => {
  console.log(`app listening on port ${port}`)
})
