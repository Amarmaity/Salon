import logo from './logo.svg';
import { useEffect, useState } from 'react';
import './App.css';
import RegisterCustomer from './components/RegisterCustomer';

function App() {
  const[file,  setFile] = useState([])

const handleData = async () => {
  try {
    const response = await fetch('http://127.0.0.1:8000/api/hello/');
    const data = await response.json();
    setFile(data); // now this will set the state properly
    console.log("data fethed succes")
  } catch (error) {
    console.error('Error fetching data:', error);
  }
};


  return (
    <div className="App">
      <button onClick={handleData} >get data</button>
      <RegisterCustomer/>
    
    </div>
  );
}

export default App;
