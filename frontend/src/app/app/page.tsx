"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPause, faPlay, faCheck, faCircleXmark} from '@fortawesome/free-solid-svg-icons';
import GetRequestExample from "./patch";

interface StatusItem {
  id: number;
  status: string;
}

export default function App() {
  const [url, setUrl] = useState("");
  const [statuses, setStatuses] = useState<StatusItem[]>([
    { id: 1, status: 'Pending' },
    { id: 2, status: 'Pending' },
    { id: 3, status: 'Pending' },
    { id: 4, status: 'Pending' },
    { id: 5, status: 'Pending' },
  ]);

  const apiEndpoint = "http://127.0.0.1:3001/api/tests"

  const fetchStatuses = async () => {
    try {
      const response = await fetch(apiEndpoint);
      if (!response.ok) {
        throw new Error(`Error: ${response.statusText}`);
      }
      const test_data = await response.json();
      const updatedStatuses: StatusItem[] = test_data.tests
      setStatuses((prevStatuses) =>
        prevStatuses.map((item) => ({
          ...item,
          status: updatedStatuses.find((u) => u.id === item.id)?.status || item.status,
        }))
      );
      console.log(statuses);
    } catch (error) {
      console.error('Error fetching statuses:', error);
    }
  };

  useEffect(() => {
    const interval = setInterval(() => {
      fetchStatuses();
    }, 1000); // Polling every 5 seconds
    return () => clearInterval(interval); // Cleanup on component unmount
  }, []);

  return (
    <>
      <div id="global">
        <div id="top-bar">
          <Link id="top-bar-logo" href="/">
            CyberAgent
          </Link>
          <div id="top-bar-nav">
            <div id="nav-expand">
              <i className="fa-solid fa-bars"></i>
            </div>
            <Link className="top-bar-btn" id="top-bar-home" href="/">
              About
            </Link>
            <Link className="top-bar-btn" id="top-bar-about" href="/app">
              App
            </Link>
          </div>
        </div>
      </div>

      <div id="main">
        <h2 className="text-center p-4">Detect</h2>
        <div id="detect" className="flex justify-center items-center space-x-4">
          <input
            id="detect-url"
            className="text-entry"
            type="text"
            placeholder="Enter URL"
            value={url}
            onChange={(text) => setUrl(text.target.value)}
          />
          <button
            id="detect-btn"
            className="button"
            onClick={async () => {
              console.log("test");
              const response = await fetch("http://127.0.0.1:3001/submit", {
                method: "POST",
                headers: {
                  "Content-Type": "application/json",
                },
                body: JSON.stringify({ input: url }),
              });
            }}
          >
            Scan for Vulnerabilities
          </button>
        </div>
        <div id="detected" className="text-block">
          <h2 className="text-center pb-4">Tests</h2>
          <table>
            <thead>
              <tr className="font-bold">
                <th className="w-1/6">#</th>
                <th className="w-1/5">Test</th>
                <th className="w-1/4">Description</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td className="td-right">1</td>
                <td>SQL Injection</td>
                <td className="text-sm">SQL injection is a security vulnerability that occurs when an attacker 
                  manipulates a web application's SQL query by injecting malicious input. </td>
                <td className="text-center">
                  {statuses[1].status == "Pending" && <FontAwesomeIcon icon={faPlay} />}
                  {statuses[1].status == "In Progress" && <FontAwesomeIcon icon={faPause} />}
                  {statuses[1].status == "Completed" && <FontAwesomeIcon icon={faCheck} />}
                </td>
              </tr>
              <tr>
                <td className="td-right">2</td>
                <td>Cross-Site Scripting</td>
                <td className="text-sm">Cross-Site Scripting (XSS) is a security vulnerability where an attacker injects 
                  malicious scripts into a web application, which are executed in the user's browser.</td>
                <td className="text-center">
                  <FontAwesomeIcon icon={faPlay} />
                </td>
              </tr>
              <tr>
                <td className="td-right">3</td>
                <td>Brute Force Attacks</td>
                <td className="text-sm">Brute force attacks are a trial-and-error method used by attackers to guess credentials, 
                  encryption keys, or other secrets by systematically trying all possible combinations.</td>
                <td className="text-center">
                  <FontAwesomeIcon icon={faPlay} />
                </td>
              </tr>
              <tr>
                <td className="td-right">4</td>
                <td>Directory Exposure</td>
                <td className="text-sm">Directory exposure occurs when a web server inadvertently allows users to view directory 
                  contents or access files not intended for public visibility.</td>
                <td className="text-center">
                <FontAwesomeIcon icon={faPlay} />
                </td>
              </tr>
              <tr>
                <td className="td-right">5</td>
                <td>Network Request Exposure</td>
                <td className="text-sm">Network request exposure occurs when sensitive data, such as API keys, tokens, or user credentials,
                  is included in unencrypted or poorly secured network requests. </td>
                <td className="text-center">
                  <FontAwesomeIcon icon={faPlay} />
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <div>
            <GetRequestExample/>s
        </div>

        <div id="footer">
          <hr />
          <div className="footer-block">
            <p>
              <b>CyberAgent</b>
            </p>
            <p>
              <Link className="link" target="_blank" href="/">
                About
              </Link>
              <br />
              <Link className="link" target="_blank" href="/app">
                App
              </Link>
            </p>
          </div>
        </div>
      </div>

      <script src="../static/src/app.js"></script>
    </>
  );
}
