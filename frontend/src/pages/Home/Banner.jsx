import React from 'react'
import BannerImg from '../../assets/banner.png'

const Banner = () => {
  return (
    <div className='flex flex-col md:flex-row-reverse py-14 justify-between items-center gap-12'>
        <div className='md:w-1/2 w-full flex items-center md:justify-end'>
            <img src={BannerImg} alt=''/>
        </div>
        <div className='md:w-1/2 w-full' >
            <h1 className='md:text-5xl text-2xl font-medium mb-7'>
                Best of the Week
            </h1>
            <p className='py-4 text-2xl text-gray-400'>
                This week’s pick is the kind of book that quietly earns a place in your hands and refuses to let go. Thoughtful, beautifully written, and impossible to rush, it’s a reminder of why we read in the first place — to slow down, to feel something, and to get lost for a while.
            </p>
        </div>
        
    </div>
  )
}

export default Banner