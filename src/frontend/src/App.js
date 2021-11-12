import {
  BrowserRouter as Router,
  Routes,
  Route
} from "react-router-dom";
import { About } from './page/About';
import { Compressor } from './page/Compressor';

function App() {
  return (
    <Router>
      <div>
        <Routes>
          <Route exact path='/about' element={ <About /> } />
          <Route exact path='/' element= { <Compressor /> } /> 
        </Routes>
      </div>
    </Router>
  );
}

export default App;
