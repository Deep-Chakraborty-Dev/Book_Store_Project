import express from 'express'
import { getAllBooks,postaBook,getSingleBook,updateBook, deleteBook } from './Bookcontroller.js';

const router = express.Router();
import Book from './Bookmodel.js';

//post a book
router.post("/createbook",postaBook)

router.get("/",getAllBooks)

router.get("/:id",getSingleBook)

router.put("/edit/:id",updateBook)

router.delete("/:id",deleteBook)

export default router;