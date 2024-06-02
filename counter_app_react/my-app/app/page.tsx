'use client';

import React, { useState, useEffect } from 'react'; // Import useState with type definition

interface LayoutProps { }



const Layout: React.FC<LayoutProps> = () => {
  const [count, setCount] = useState<number>(0);
console.log(process.env.NEXT_PUBLIC_COUNTER_API_URL);
  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch(process.env.NEXT_PUBLIC_COUNTER_API_URL);

      const data = await response.json();
      setCount(data.counter);
    }

    fetchData()
      // make sure to catch any error
      .catch(console.error);;
  })

  const handleClick = async () => {
    try {
      const response = await fetch(process.env.REACT_APP_COUNTER_API_URL, {
        method: 'POST'
      });

      if (!response.ok) {
        throw new Error(`API request failed with status ${response.status}`);
      }

      const data = await response.json();
      setCount(data.counter);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  return (
    <div className="container">
      <div className="row">
        <h1 className="text-4xl font-bold">Counter</h1>
        <div className="text-2xl font-bold">{count}</div>
      </div>
      <div className="row">
        <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" onClick={handleClick}>
          Click!
        </button>
      </div>
    </div>
  );
};

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">

      <Layout />

    </main>
  );
}
