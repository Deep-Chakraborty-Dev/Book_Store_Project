import Order from "./order.model.js"

export const createAnOrder = async(req,res) => {
    try {
        const newOrder = await Order(req.body)
        const saveOrder = await newOrder.save()
        res.status(200).json(saveOrder)
    } catch (error) {
        console.log("Error while creating an Order..",error)
        res.status(500).send({message:"Failed to create an Order"},error)
    }
}

export const getOrderByEmail = async (req, res) => {
  try {
    const { email } = req.params;
    console.log(`query orders for ${email}`);

    const orders = await Order.find({ email }).sort({ createdAt: -1 });

    // always return the list (empty if none found); front end handles the "no
    // orders" case.  Avoid treating emptiness as a 404 so the client doesn't
    // enter the error state.
    res.status(200).json(orders);

  } catch (error) {
    console.error("Error fetching orders", error);
    res.status(500).json({ message: "Failed to fetch order" });
  }
};