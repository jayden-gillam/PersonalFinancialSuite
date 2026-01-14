import {useEffect, useState} from 'react'
import {getIncome, addIncome} from "../api.js";
import './App.css'

function App() {
  const [data, setData] = useState([])

  const [source, setSource] = useState(null);
  const [gross, setGross] = useState(null);
  const [net, setNet] = useState(null);
  const [date, setDate] = useState(null);
  const [notes, setNotes] = useState(null);

  useEffect(() => {
      getIncome().then(data => setData(data))
    },
    [])

  const handleSubmit = async (e) => {
    e.preventDefault();

    const income = {
      income_source: source,
      gross_amount: gross,
      net_amount: net,
      income_date: date,
      income_notes: notes
    };

    await addIncome(income);

    const updated = await getIncome();
    setData(updated);

    setSource("");
    setGross("");
    setNet("");
    setDate("");
    setNotes("");
  };



  return (
    <>
      <table>
        <thead>
          <tr>
            <th>Source</th>
            <th>Gross Income</th>
            <th>Net Income</th>
            <th>Date</th>
            <th>Notes</th>
          </tr>
        </thead>
        <tbody>
          {data.map(item => (
            <tr key={item.income_id}>
              <td>{item.income_source}</td>
              <td>{item.gross_amount}</td>
              <td>{item.net_amount}</td>
              <td>{item.income_date}</td>
              <td>{item.income_notes}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <form onSubmit={handleSubmit}>
        <label>Source:</label>
        <input value={source} onChange={e => setSource(e.target.value)} />

        <label>Gross:</label>
        <input value={gross} onChange={e => setGross(e.target.value)} />

        <label>Net:</label>
        <input value={net} onChange={e => setNet(e.target.value)} />

        <label>Date:</label>
        <input type="date" value={date} onChange={e => setDate(e.target.value)} />

        <label>Notes:</label>
        <input value={notes} onChange={e => setNotes(e.target.value)} />

        <button type="submit">Add Income</button>
      </form>
    </>
  );
}

export default App
