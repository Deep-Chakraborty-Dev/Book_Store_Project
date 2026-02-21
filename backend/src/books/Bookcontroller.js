import Book from "./Bookmodel.js"

export const postaBook = async (req,res)=>{
    try {
        const newBook = await Book({...req.body})
        await newBook.save()
        res.status(200).send({message:"Book created succesfully!",book:newBook})
    } catch (error) {
        console.log("Error while creating a book..",error)
        res.status(500).send({message:"Failed to create a book"},error)
    }
}

export const getAllBooks = async (req,res) => {
    try {
        const books = await Book.find().sort({createdAt:-1});
        res.status(200).json(books)
    } catch (error) {
        console.log("Error while fetching the books..",error)
        res.status(500).json({message:"Failed to fetch the books"},error)
    }
}

export const getSingleBook = async (req,res) => {
    try {
        const {id} = req.params;
        const book = await Book.findById(id);
        if(!book){
            res.status(404).send("book not found")
        }
        res.status(200).send(book)
    } catch (error) {
        console.log("Error while fetching the book..",error)
        res.status(404).send({message:"Failed to fetch the book"},error)
    }
}

export const updateBook = async (req,res) => {
    try {
        const {id} = req.params;
        const updatedBook = await Book.findByIdAndUpdate(id,req.body,{new:true})
        if(!updatedBook){
            res.status(404).send("book not updated")
        }
        res.status(200).send({
            message:"book updated successfully!",
            book:updatedBook
        })
    } catch (error) {
        console.log("Error while updating the book..",error)
        res.status(500).send({message:"Failed to update the book"},error)
    }
}

export const deleteBook = async (req,res) => {
    try {
        const {id} = req.params;
        const deletedBook = await Book.findByIdAndDelete(id)
        if(!deletedBook){
            res.status(404).send("book not deleted")
        }
        res.status(200).send({
            message:"book deleted successfully!",
            book:deletedBook
        })
    } catch (error) {
        console.log("Error while deleting the book..",error)
        res.status(500).send({message:"Failed to delete the book"},error)
    }
}
