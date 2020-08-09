import React from 'react';
import './styles/App.css';
import {useRoutes} from "./routes";

export const App = () => {
  const routes = useRoutes()

  return (
    <div className="App">
        {routes}
    </div>
  );
}
