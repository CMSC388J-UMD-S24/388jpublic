import { useState, useMemo, useEffect } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0);

  const doubledCount = useMemo(() => count * 2, [count]);
  const isEven = useMemo(() => count % 2 === 0, [count]);

  useEffect(() => {
    document.title = `${count}`;
  }, [count]);

  function increment() {
    setCount((count) => count + 1);
  }

  return (
    <div className="counter">
      <button onClick={increment}>
        count is {count}
      </button>
      <p>
        {count} x 2 = {doubledCount}
      </p>
      <p>
        {count} is {isEven ? 'even' : 'odd'}
      </p>
    </div>
  );
}