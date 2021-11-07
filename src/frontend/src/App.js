import './App.css';
import React,{useState, useEffect} from 'react';
import Main from './components/Main';

function App() {
  
  const [currentTime, setCurrentTime] = useState(0);
  
  useEffect(() => {

    fetch('/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);

    });

  }, []);

  

  return (
    <div className="App">
      <header className="App-header">
        <a
          className="App-link"
          href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
          target="_blank"
          rel="noopener noreferrer"
        >
          Selamat Mengkuli
        </a>
        <p>Waktu sekarang adalah <br/>{currentTime}.</p>
      </header>
      <h1>Upload Image</h1>
      <Main />
    </div>
  );
}

export default App;
