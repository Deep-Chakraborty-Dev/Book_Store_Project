import express from 'express'
import { createAnOrder, getOrderByEmail } from './order.controller.js';

const router = express.Router();

router.post('/',createAnOrder)

router.get('/email/:email',getOrderByEmail)

export default router