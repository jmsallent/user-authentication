import mongoose from "mongoose";

const connect = async () =>{
    try {
        await mongoose.connect('mongodb://127.0.0.1:27017/my_db');
        console.log("CONNECTED TO THE DB!")
    } catch (error) {
        console.log(error)
    }
    
}
connect()