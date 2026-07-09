import React from 'react'
import { FiShoppingCart } from "react-icons/fi"
import { getImgUrl } from '../../utils/getImgUrl'
import {Link} from 'react-router-dom'
import {useDispatch} from 'react-redux'
import { addtoCart } from '../../redux/features/cart/cartSlice'


const BookCard = ({book}) => {
  const dispatch = useDispatch();

  const handleaddtoCart = (product) => {
    dispatch(addtoCart(product))
  }

  return (
    <div className="rounded-3xl bg-white shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-2xl">
      <div className="flex flex-col sm:flex-row sm:items-center sm:h-72 sm:justify-between gap-5 p-5">
        <div className="sm:h-72 sm:shrink-0 border border-slate-200 rounded-2xl overflow-hidden bg-slate-50">
          <Link to={`/books/${book._id}`}>
            <img
              src={getImgUrl(book.coverImage)}
              alt={book.title}
              className="w-full h-full object-cover rounded-2xl cursor-pointer transition-transform duration-200 hover:scale-105"
            />
          </Link>
        </div>

        <div className="flex-1">
          <Link to={`/books/${book._id}`}>
            <h3 className="text-xl font-semibold hover:text-blue-600 mb-3">
              {book.title}
            </h3>
          </Link>
          <p className="text-gray-600 mb-5">
            {book.description.length > 80
              ? `${book.description.slice(0, 80)}...`
              : book.description}
          </p>
          <p className="font-medium mb-5">
            {book?.newPrice}{' '}
            <span className="line-through font-normal ml-2">{book?.oldPrice}</span>
          </p>
          <button
            onClick={() => handleaddtoCart(book)}
            className="btn-primary px-6 space-x-1 flex items-center gap-1"
          >
            <FiShoppingCart />
            <span>Add to Cart</span>
          </button>
        </div>
      </div>
    </div>
  )
}

export default BookCard