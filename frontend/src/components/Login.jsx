import React, { useEffect, useState } from 'react'
import { Link, useNavigate } from "react-router-dom";
import { FaGoogle } from "react-icons/fa";
import { useForm } from "react-hook-form"
import { useAuth } from '../context/AuthContext';


const Login = () => {
    const navigate = useNavigate();
    const [message,setMessage]=useState("")
    const {
        register,
        handleSubmit,
        watch,
        formState: { errors },
        reset,
  } = useForm()

  const {loginUser,signInWithGoogle} = useAuth()

  const onSubmit = async (data) => {
    try {
        await loginUser(data.email,data.password)
        alert("login successfull")
        navigate("/")
        
    } catch (error) {
        setMessage("Please provide a valid email or password")
        console.log(error);
    }
  }

  const handleGoogleSignIn = async () => {
    try {
        await signInWithGoogle()
        alert("Successfully Login with google")
    } catch (error) {
        alert("failed to login with google ")
    }
  }

  useEffect(()=>{
    reset({
        email:'',
        password:''
    }
    )
  },[reset])

  return (
    <div className='h-[calc(100vh-120px)] flex justify-center items-center'>
        <div className='w-full max-w-sm mx-auto bg-white rounded-2xl px-8 pt-6 pb-8 mb-4 shadow-2xl'>
            <h2 className='text-xl font-semibold mb-4'>
                Login
            </h2>
            <form onSubmit={handleSubmit(onSubmit)} autoComplete='off'>
                <div className='mb-4'>
                    <label className='block text-gray-700 text-sm font-bold mb-2' htmlFor='email'>Email
                    </label>
                    <input 
                    {...register("email", { required: true })}
                    type='email' id='email' autoComplete='off' name='email' placeholder='example@mail.com'
                    className='shadow appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow'>
                        </input>
                </div>

                <div className='mb-4'>
                    <label className='block text-gray-700 text-sm font-bold mb-2' htmlFor='password'>Password
                    </label>
                    <input 
                    {...register("password", { required: true })}
                    type='password' id='password' name='password' placeholder='password'
                    className='shadow appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow'>
                        </input>
                </div>

                {
                    message && <p className='text-red-500 text-sm italic mb-2'>{message}</p>
                }

                <div>
                    <button className='bg-blue-500 hover:bg-blue-700 tex-white font-bold rounded focus:outline-none p-2'>
                        Login
                    </button>
                </div>

                <p className='font-medium mt-4 text-sm'>
                    Haven't got an account? 
                    <Link to='/register' className='ml-1 text-blue-500 hover:text-blue-700'>Register Here</Link>
                </p>

                {/*google icon*/}
                <div>
                    <button 
                    onClick={handleGoogleSignIn}
                    className='w-full flex flex-wrap gap-1 items-center justify-center bg-black text-white py-2 px-1 mt-2 hover:bg-blue-500 focus:outline-none rounded'>
                        <FaGoogle className='mr-2'/>
                        Sign it with Google
                    </button>
                </div>
                 <div className='mt-4 text-center text-gray-500 tex-xs'>
                    © {new Date().getFullYear()} Book Nest. All rights reserved.
                </div>
            </form>
        </div>
    </div>
  )
}

export default Login