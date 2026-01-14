const API_URL = import.meta.env.VITE_API_URL;

export const getIncome = async () => {
  const res = await fetch(`${API_URL}/income`)
  return res.json()
}

export const addIncome = async (income) => {
  const res = await fetch(`${API_URL}/income`, {
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify(income)
  })
  console.log(res)

  return res.json()
}