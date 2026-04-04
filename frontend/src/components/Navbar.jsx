import React, { useState } from 'react'
import { Link } from 'react-router'
import { FaBarsStaggered } from "react-icons/fa6";
import { BsSearch } from "react-icons/bs";
import { FaRegUser } from "react-icons/fa";
import { GoHeart } from "react-icons/go";
import { FaShoppingCart } from "react-icons/fa";
import avatarImg from "../assets/avatar.png"
import { useSelector } from 'react-redux';
import { useAuth } from '../context/AuthContext';

const navigation = [
    {name:"Cart Page", href:"/cart"},
    {name:"Orders", href:"/orders"},
    {name:"Check Out", href:"/checkout"},
]

const Navbar = () => {

  const {currentUser,logout} = useAuth()

  const handleLogOut = () => {
    logout()
  }

  const [isDropDownOpen,setIsDropDown] = useState(false)
  console.log(isDropDownOpen)

  const cartItems = useSelector(state => state.cart.cartItems);
  console.log(cartItems)

  return (
    <header className='max-w-screen-2xl mx-auto px-4 py-6 sticky top-0 bg-white shadow-md z-50'>
        <nav className='flex justify-between items-center'>

            {/*left side*/}
            <div className='flex items-center md:gap-10 gap-4'>

            <div className='flex flex-row text-2xl font-bold items-center underline text-amber-400 transition-transform duration-150 ease-out hover:scale-125'>
                <Link to={'/'}>BOOKNEST</Link></div>

                
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
                              <div className='absolute right-0 mt-2 w-40 shadow-lg z-40  rounded-2xl opacity-95'>
                                    <ul className='py-2'>
                                        {
                                            navigation.map((item)=>(
                                                <li key={item.name}>
                                                    <Link to={item.href}
                                                    className='block px-4 py-2 text-sm  bg-gray-400   hover:bg-gray-500 transition-transform duration-150'>
                                                    {item.name}
                                                    </Link>
                                                </li>
                                            ))
                                        }
                                        <li>
                                            
                                            <button onClick={() => handleLogOut()}
                                            className='block w-full text-left px-4 py-2 text-sm bg-red-400 hover:bg-red-500 transition-transform duration-150'>
                                                Logout
                                            </button>
                                        </li>
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