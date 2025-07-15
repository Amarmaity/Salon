import { useState } from 'react';
import './App.css';
import RegisterCustomer from './components/RegisterCustomer';

function App() {
  const [file, setFile] = useState([]);

  const handleData = async () => {
    try {
      const response = await fetch('https://salon-oa03.onrender.com/api/hello/');
      const data = await response.json();
      setFile(data);
      console.log("data fetched successfully");
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  return (
    <div className="App">
      <button onClick={handleData}>Get Data</button>
      <RegisterCustomer />
      
      {file.length > 0 && (
        <pre>{JSON.stringify(file, null, 2)}</pre>
      )}
    </div>
  );
}

export default App;
