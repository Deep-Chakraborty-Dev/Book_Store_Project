import React from 'react'
import { useGetOrderByEmailQuery } from '../../redux/features/orders/ordersApi'
import { useFetchAllBooksQuery } from '../../redux/features/books/booksapi'
import { useAuth } from '../../context/AuthContext'

const OrderPage = () => {
  const { currentUser } = useAuth()

  // Fetch orders
  const { data: orders = [], isLoading, isError } = useGetOrderByEmailQuery(currentUser?.email, {
    skip: !currentUser?.email
  })

  // Fetch all books
  const { data: books = [], isLoading: booksLoading } = useFetchAllBooksQuery()

  if (isLoading || booksLoading) return <div>Loading...</div>
  if (isError) return <div>Error getting orders data</div>

  return (
    <div className="container mx-auto p-6">
      <h2 className="text-2xl font-semibold mb-4">Your Orders</h2>

      {orders.length === 0 ? (
        <div>No orders found!</div>
      ) : (
        <div>
          {orders.map((order, index) => (
            <div key={order._id} className="border-b mb-4 pb-4">
              <p className="p-1 bg-secondary text-white w-10 rounded mb-1"># {index + 1}</p>
              <h2 className="font-bold">Order ID: {order._id}</h2>
              <p className="text-gray-600">Name: {order.name || 'N/A'}</p>
              <p className="text-gray-600">Email: {order.email || 'N/A'}</p>
              <p className="text-gray-600">Phone: {order.phone || 'N/A'}</p>
              <p className="text-gray-600">Total Price: ${order.totalPrice || 0}</p>

              <h3 className="font-semibold mt-2">Address:</h3>
              <p>
                {order.address?.city || 'N/A'}, {order.address?.state || 'N/A'}, {order.address?.country || 'N/A'}, {order.address?.zipcode || 'N/A'}
              </p>

              <h3 className="font-semibold mt-2">Products:</h3>
              <ul>
                {/** primary data comes from `productIds` stored in the order.  older
                    code may have used `products` but the schema now uses productIds **/}
                {order.productIds && order.productIds.length > 0 ? (
                  order.productIds.map(id => {
                    const book = books.find(b => String(b._id) === String(id))
                    return <li key={id}>{book?.title || id}</li>
                  })
                ) : (
                  <li>No products found</li>
                )}
              </ul>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

export default OrderPage
