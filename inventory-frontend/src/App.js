import { Products } from './components/Products';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import logo from './logo.svg';



function App() {
  return <BrowserRouter>
    <Routes>
        <Route path="/" element={<Products />} />
    </Routes>
  </BrowserRouter>
}

export default App;
