import React from 'react'
import BookCard from '../Books/BookCard'
import { Swiper, SwiperSlide } from 'swiper/react';
import { useState, useEffect } from 'react';
import { useFetchAllBooksQuery } from '../../redux/features/books/booksapi';
import { Pagination , Navigation } from 'swiper/modules';

// Import Swiper styles
import 'swiper/css';
import 'swiper/css/bundle';
import 'swiper/css/pagination';
import 'swiper/css/navigation';

const Recommended = () => {

   const {data: books=[]} = useFetchAllBooksQuery();


  return (
    <div>
        <h2 className='text-3xl py-6 font-semibold mb-6'>Reccomended</h2>

        <Swiper
            slidesPerView={1}
            spaceBetween={30}
            navigation={true}
            
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
            className="mySwiper"
          >
            
            {
                books.length>0 && books.slice(8,16).map((book,index) => (
                  <SwiperSlide className='py-3' key={index}><BookCard book={book}/></SwiperSlide>
                  
                ))
              }
          </Swiper>
    </div>
  )
}

export default Recommended