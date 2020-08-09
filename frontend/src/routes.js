import React from "react";
import {BrowserRouter, Redirect, Route, Switch} from "react-router-dom";
import {StartPage} from "./pages/StartPage";


export const useRoutes = () => {
  return (
    <BrowserRouter>
      <Switch>
        <Route path="/" component={StartPage} exact />
        <Redirect push to="/" />
      </Switch>
    </BrowserRouter>
  )
}