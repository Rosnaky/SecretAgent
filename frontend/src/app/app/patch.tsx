import React, { useState, useEffect } from "react";

const GetRequestExample: React.FC = () => {
  const [data, setData] = useState<{ recommendations: string; issues: string } | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("http://127.0.0.1:5000/api/data"); // Replace with your backend URL
        if (!response.ok) {
          throw new Error(`Error: ${response.status}`);
        }
        const responseData = await response.json();
        setData(responseData);
      } catch (err: any) {
        setError(err.message);
      }
    };

    fetchData();
  }, []); // Empty dependency array ensures it runs once on component mount

  return (
    <div>
      <h1>Data from Backend</h1>
      {data ? (
        <div>
          <p><strong>Recommendations:</strong> {data.recommendations}</p>
          <p><strong>Issues:</strong> {data.issues}</p>
        </div>
      ) : error ? (
        <p style={{ color: "red" }}>Error: {error}</p>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default GetRequestExample;
