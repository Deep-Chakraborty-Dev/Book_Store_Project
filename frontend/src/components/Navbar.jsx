import React, { useState } from 'react'
import { Link } from 'react-router'
import { FaBarsStaggered } from "react-icons/fa6";
import { BsSearch } from "react-icons/bs";
import { FaRegUser } from "react-icons/fa";
import { GoHeart } from "react-icons/go";
import { FaShoppingCart } from "react-icons/fa";
import avatarImg from "../assets/avatar.png"
import { useSelector } from 'react-redux';

const navigation = [
    {name:"Dashboard", href:"/dashboard"},
    {name:"Cart Page", href:"/cart"},
    {name:"Orders", href:"/orders"},
    {name:"Check Out", href:"/checkout"},
]

const Navbar = () => {
  const currentUser = true;
  const [isDropDownOpen,setIsDropDown] = useState(false)
  console.log(isDropDownOpen)

  const cartItems = useSelector(state => state.cart.cartItems);
  console.log(cartItems)

  return (
    <header className='max-w-screen-2xl mx-auto px-4 py-6 sticky top-0 bg-white shadow-md z-50'>
        <nav className='flex justify-between items-center'>

            {/*left side*/}
            <div className='flex items-center md:gap-10 gap-4'>
                <Link to="/">
                <FaBarsStaggered className='size-6'/>
                </Link>

            <div className='flex flex-row text-2xl font-bold items-center underline text-amber-400'>
                <Link to={'/'}>BOOKNEST</Link></div>

            <div className='relative'>
                {/*search bar*/}
                <Link to="/">
                <BsSearch className='absolute inline-block left-3 inset-y-2' />
                <input type='text' placeholder='Search...' className='bg-blue-100 w-full py-1 md:px-8 px-6 rounded-md focus:outline-none'></input>
                </Link>
            </div>

                
            </div>
        <div className='relative flex items-center sm:space-x-3 space-x-2'>
            {/*rigt side*/}
            <div>
                {
                    currentUser ? <>
                        <button onClick={() => setIsDropDown(!isDropDownOpen)}>
                            <img src={avatarImg} alt="" className={`size-7 rounded-full ${currentUser ? 'ring-2 ring-violet-400' : ""}`} />
                        </button>

                        {/*show dropdowns*/}
                        {
                            isDropDownOpen && (
                              <div className='absolute right-0 mt-2 w-40 bg-primary shadow-lg rounded-md z-40'>
                                    <ul className='py-2'>
                                        {
                                            navigation.map((item)=>(
                                                <li key={item.name}>
                                                    <Link to={item.href}
                                                    className='block px-4 py-2 text-sm  hover:bg-amber-500'>
                                                    {item.name}
                                                    </Link>
                                                </li>
                                            ))
                                        }
                                    </ul>
                                </div>
                            )
                        }


                    </> :<Link to="/login">
                    <FaRegUser className='size-6'/>
                    </Link>
                }
            </div>
            
            <button className='hidden sm:block'>
                <GoHeart className='size-6'/>
            </button>   
            
            <Link to="/cart" className='bg-primary p-1 sm:px-6 px-2 flex items-center rounded-sm'>
            <FaShoppingCart/>
                {
                    cartItems.length>0 ? <span className='text-sm font-semibold sm:ml-1 py-2 rounded-2xl'>
                        {cartItems.length}
                    </span> : <span className='text-sm font-semibold sm:ml-1 py-2 rounded-2xl'>
                        0
                    </span>

                }
            
            </Link>
        </div>
        </nav>

    </header>
  )
}

export default Navbar