import express from "express";
import morgan from "morgan";
import * as db from "./db/db.js"
import {routes as registerRoutes} from "./routes/register.router.js"

export const app = express()
app.set('view engine', 'ejs');
app.use(express.json())

app.use("/register", registerRoutes);

