import express from 'express'
import mongoose from 'mongoose';
import dotenv from 'dotenv'
import cors from 'cors'

// Correcting the imports to match their purpose
import bookRoutes from './src/books/Bookroute.js' 
import orderRoutes from './src/orders/order.route.js'
import userRoutes from './src/users/user.route.js'
import adminRoutes from './src/stats/admin.stats.js'

dotenv.config();
const app = express()
const port = process.env.PORT || 5000

app.use(express.json());

// Add both ports to CORS since your Vite sometimes runs on 5174

app.use(cors({
  origin: ['http://localhost:5173', 'http://localhost:5174'],
  credentials: true
}))

// Correctly assigning the routes
app.use('/api/books', bookRoutes)   // Books path -> Book logic
app.use('/api/orders', orderRoutes) // Orders path -> Order logic
app.use('/api/auth',userRoutes)
app.use("/api/admin", adminRoutes)

async function main() {
  const uri = process.env.DB_URL;
  if (!uri) {
    console.error('DB_URL environment variable is not set');
    process.exit(1);
  }

  // add some options to avoid deprecation warnings and help with buffering
  await mongoose.connect(process.env.DB_URL);

  mongoose.connection.on('error', err => {
    console.error('MongoDB connection error:', err);
  });

  // root route can be declared here without blocking the rest of the app
  app.get('/', (req, res) => {
    res.send('Book server is listening')
  })
}

main().then(() => console.log("mongodb connected successfully!")).catch(err => console.log(err));

app.listen(port, () => {
  console.log(`app listening on port ${port}`)
})