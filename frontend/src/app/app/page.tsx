"use client";

import { useState, useEffect } from "react";
import Link from "next/link";

export default function App() {
  const [url, setUrl] = useState("");
  const [progresses, setProgresses] = useState(["", "", "", ""]);
  const [fixes, setFixes] = useState(["", "", "", ""]);

  useEffect(() => {
    const interval = setInterval(async () => {
      const response = await fetch("http://127.0.0.1:3001/status");
      const result = await response.json();
      setProgresses(result.filter((x: { status: string }) => x.status));
      setFixes(
        result.filter((x: { recommendations: string }) => x.recommendations)
      );
    }, 500);

    return () => clearInterval(interval);
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
        <div id="about" className="text-block">
          <h2>About CyberAgent</h2>
          <p>yes</p>
        </div>

        <div id="detect" className="text-block">
          <h2>Detect</h2>
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

              // Handle the response
              const result = await response.json();
              console.log("Server response:", result);
              alert("Server response: " + JSON.stringify(result));
            }}
          >
            Scan for Vulnerabilities
          </button>
        </div>

        <div id="detected" className="text-block">
          <h2>Detected Vulnerabilities</h2>
          <p id="detected-status">Scanning... (x%)</p>
          <table>
            <tr>
              <th>#</th>
              <th>Issue</th>
              <th>Description</th>
              <th>Recommended Fix</th>
              <th>Progress</th>
            </tr>
            <tr>
              <td className="td-right">1</td>
              <td>SQL Injection</td>
              <td>
                In computing, SQL injection is a code injection technique used
                to attack data-driven applications, in which malicious SQL
                statements are inserted into an entry field for execution (e.g.
                to dump the database contents to the attacker). SQL injection
                must exploit a security vulnerability in an application's
                software, for example, when user input is either incorrectly
                filtered for string literal escape characters embedded in SQL
                statements or user input is not strongly typed and unexpectedly
                executed.
              </td>
              <td>{fixes[0]}</td>
              <td>{progresses[0]}</td>
            </tr>
            <tr>
              <td className="td-right">2</td>
              <td>Cross-site Scripting (XSS)</td>
              <td>
                Cross-Site Scripting (XSS) attacks are a type of injection, in
                which malicious scripts are injected into otherwise benign and
                trusted websites. XSS attacks occur when an attacker uses a web
                application to send malicious code, generally in the form of a
                browser side script, to a different end user.
              </td>
              <td>{fixes[1]}</td>
              <td>{progresses[1]}</td>
            </tr>
            <tr>
              <td className="td-right">1</td>
              <td>Brute-force attack</td>
              <td>
                A brute-force attack consists of an attacker submitting many
                passwords or passphrases with the hope of eventually guessing
                correctly.
              </td>
              <td>{fixes[2]}</td>
              <td>{progresses[2]}</td>
            </tr>
            <tr>
              <td className="td-right">1</td>
              <td>Exposed Directories</td>
              <td>
                An exposed directories vulnerability is a security flaw in a web
                server that allows unauthorized users to view the contents of
                directories on a website.
              </td>
              <td>{fixes[3]}</td>
              <td>{progresses[3]}</td>
            </tr>
          </table>
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
