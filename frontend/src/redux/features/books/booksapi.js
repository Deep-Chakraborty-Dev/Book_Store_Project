import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'
import getbaseUrl from '../../../utils/baseURL'


const baseQuery = fetchBaseQuery({
    baseUrl:`${getbaseUrl()}api/books`,
    credentials: 'include',
    prepareHeaders: (Headers) => {
        const token = localStorage.getItem('token');
        if(token){
            Headers.set('Authorization',`Bearer ${token}`);
        }
        return Headers
    }
})

const booksApi = createApi({
    reducerPath: 'bookApi',
    baseQuery,
    tagTypes:['Books'],
    endpoints: (builder) => ({
        fetchAllBooks:builder.query({
            query: () => "/",
            providesTags:["Books"]
        })
    })
})

export const {useFetchAllBooksQuery} = booksApi;
export default booksApi;
