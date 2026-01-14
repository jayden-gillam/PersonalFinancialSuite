import {useEffect, useState} from 'react'
import './App.css'

function App() {
  const API_URL = import.meta.env.VITE_API_URL;
  const [data, setData] = useState([])

  const getIncome = async () => {
    const res = await fetch(`${API_URL}/income`)
    return res.json()
  }

  useEffect(() => {
      getIncome().then(data => setData(data))
    },
    [])

  return (
      <>
        {data.map(item => (
          <div key={item.income_id}>
            {item.income_source} - ${item.net_amount}
          </div>
        ))}
      </>
  )
}

export default App
