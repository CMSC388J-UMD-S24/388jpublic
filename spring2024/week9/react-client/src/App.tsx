import './App.css'

import Counter from './components/Counter'
import Loops from './components/Loops'
import Card from './components/Card'

function App() {
  return (
    <>
      <div className="card">
        <Counter />
        <Loops />
        <Card title="Card title">
          <p>Card content</p>
          <a>link</a>
        </Card>
      </div>
    </>
  )
}

export default App
