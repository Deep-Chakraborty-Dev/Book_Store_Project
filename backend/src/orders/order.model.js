import mongoose from "mongoose";

const orderSchema = new mongoose.Schema({
    name : {
        type:String,
        required:true
    },
    email : {
        type:String,
        required:true
    },
    address : {
            city : {
            type:String,
            required:true
        },
        country: String,
        state: String,
        zipcode:String,
    },
    phone : {
        type:Number,
        required : true,
    },
    // deliberately use singular "productIds" to match frontend code
    productIds: [
        {
            type: mongoose.Schema.Types.ObjectId,
            ref: 'BOOK',
            required: true
        }
    ],
    totalPrice : {
        type:Number,
        required : true,
    }
},{
    timestamps : true
})

const Order = mongoose.model('Order',orderSchema)

export default Order