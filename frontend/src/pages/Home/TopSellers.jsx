import React, { useEffect, useState } from 'react'
import BookCard from '../Books/BookCard'
import { Swiper, SwiperSlide } from 'swiper/react';

import { Pagination , Navigation } from 'swiper/modules';

// Import Swiper styles
import 'swiper/css';
import 'swiper/css/bundle';
import 'swiper/css/pagination';
import 'swiper/css/navigation';
import { useFetchAllBooksQuery } from '../../redux/features/books/booksapi';



const category = ["Choose a genre","Business","Fiction","Horror","Adventure"]
const TopSellers = () => {

    const [selectedcategory,Setselectedcategory] = useState("choose a genre")

    const { data: books = [], isLoading, isError, error } = useFetchAllBooksQuery();

      if (isLoading) return <div>Loading Books...</div>;
      if (isError) return <div>Error: {error?.message || "Could not fetch books"}</div>;

    const filteredBooks = selectedcategory === "choose a genre" ?
                                                books : books.filter(book =>
                                                book.category.toLowerCase() === selectedcategory.toLowerCase())

    

  return (
    <div className='py-10 px-4 md:px-6 top-sellers-section'>
        <div className='mb-8 flex flex-col gap-4 sm:flex-row sm:items-end sm:justify-between'>
          <div>
            <h2 className='text-3xl sm:text-4xl font-semibold mb-2 top-sellers-title'>Top Sellers</h2>
            <p className='text-sm text-slate-500 max-w-2xl'>Browse our best-rated books with a smooth swipe experience and filter by genre.</p>
          </div>
          <div className='flex flex-col gap-3 sm:flex-row sm:items-center top-sellers-filter'>
            <label htmlFor='category' className='text-sm font-medium text-slate-700'>Filter by genre</label>
            <select
              onChange={(e) => Setselectedcategory(e.target.value)}
              name='category' id='category' className='border bg-white border-gray-300 rounded-xl px-4 py-3 focus:outline-none focus:border-yellow-400 focus:ring-2 focus:ring-yellow-100 top-sellers-select'>
                {
                  category.map((category,index ) => (
                    <option key={index} value={category}>{category}</option>
                  ))
                }
            </select>
          </div>

              <Swiper
            slidesPerView={1}
            spaceBetween={30}
            navigation={true}
            className="mySwiper top-sellers-swiper"
            
            breakpoints={{
              640: {
                slidesPerView: 1,
                spaceBetween: 20,
              },
              768: {
                slidesPerView: 2,
                spaceBetween: 40,
              },
              1024: {
                slidesPerView: 2,
                spaceBetween: 50,
              },
              1180: {
                slidesPerView: 3,
                spaceBetween: 50,
              },
            }}
            modules={[Pagination ,Navigation]}
          >
            
            {
                filteredBooks.length>0 && filteredBooks.map((book,index) => (
                  <SwiperSlide key={index}><BookCard book={book}/></SwiperSlide>
                  
                ))
              }
          </Swiper>
            
              
    </div>

  )
}

export default TopSellers