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
    <div className='py-10 top-sellers-section'>
        <h2 className='text-3xl font-semibold mb-6 top-sellers-title'>Top Sellers</h2>
          <div className='mb-32 flex items-center top-sellers-filter'>
            <select
            onChange={(e) => Setselectedcategory(e.target.value)}
            name='category' id='category' className='border bg-amber-50 border-gray-300 rounded-md px-4 py-2 focus:outline-none top-sellers-select'>
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