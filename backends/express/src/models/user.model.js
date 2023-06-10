import mongoose from 'mongoose';

const modelSchema = mongoose.Schema(
    {
        email: String, 
        name: String,
        password: String,
    }
);

export const User = mongoose.model('user', modelSchema);
