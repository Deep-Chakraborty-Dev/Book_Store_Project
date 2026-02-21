import React from 'react'
import Banner from './Banner'
import TopSellers from './TopSellers'
import Reccomended from './Recommended'
import News from './News'

const Home = () => {
  return (
    <>
        <Banner/>
        <TopSellers/>
        <Reccomended/>
        <News/>
    </>
  )
}

export default Home