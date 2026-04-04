import express from 'express'
import { getAllBooks,postaBook,getSingleBook,updateBook, deleteBook } from './Bookcontroller.js';
import verifyAdminToken from '../middleware/verifyAdminToken.js';

const router = express.Router();
import Book from './Bookmodel.js';

//post a book
router.post("/createbook",verifyAdminToken, postaBook)

router.get("/",getAllBooks)

router.get("/:id",getSingleBook)

router.put("/edit/:id",verifyAdminToken,updateBook)

router.delete("/:id",verifyAdminToken,deleteBook)

export default router;