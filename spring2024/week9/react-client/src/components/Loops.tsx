export default function Loops() {
  const array= [1, 2, 3]
  return (
    <>
      <h2>Loops</h2>
      <ul>
        {array.map((number) => (
          <li key={number}>{number}</li>
        ))}
      </ul>
    </>
  )
}
