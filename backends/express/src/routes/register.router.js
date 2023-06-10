import { Router } from 'express';

// import all controllers
// import SessionController from './app/controllers/SessionController';

export const routes = new Router();

// Add routes
routes.get('/', (req, res) =>{
    res.render("register");
});
routes.post('/', (req, res) =>{
    res.render("register");
});